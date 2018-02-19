from django.conf import settings
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
#from django.db.models.functions import Coalesce

# Create your views here.
from django.http import HttpResponse
from .models import tblResults, tblActionLog
from datetime import datetime, date, time


SP_INIT     = 1
SP_SWIM     = 2
SP_TR1      = 3
SP_CICLE    = 4
SP_TR2      = 5
SP_RUN      = 6
SP_FINISHED = 7

ACT_LOGIN          = 100
ACT_LOGOUT         = 101
ACT_TAP_START      = 102
ACT_TAP_SPORTSMAN  = 103

class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True


def case(*args):
    return any((arg == switch.value for arg in args))


def SportsmanState(s_id):
    result = tblResults.objects.filter(res_Sportsman__exact=s_id)[0]
    if result.res_EndRunTime != None:
        return SP_FINISHED
    elif result.res_StartRunTime != None:
        return SP_RUN
    elif result.res_EndCicleTime != None:
        return SP_TR2
    elif result.res_StartCicleTime != None:
        return SP_CICLE
    elif result.res_EndSwimTime != None:
        return SP_TR1
    elif result.res_StartSwimTime != None:
        return SP_SWIM
    else:
        return SP_INIT


def index(request):
#    return render_template('signup.html')
    return HttpResponse("Hello, world. You're at the polls index.")


def dbSaveAction(user, action_id, action_desc):
    tblActionLog.add(user, timezone.now(), action_id, action_desc)


def tapSportsman(request, sportsman_id):
    results = tblResults.objects.filter(res_Sportsman__exact=sportsman_id)
    result = results[0]
    sportsmanState = SportsmanState(sportsman_id)
    while switch(sportsmanState):
        if case(SP_INIT):
            results.update(res_StartSwimTime = timezone.now())
            break
        if case(SP_SWIM):
            results.update(res_EndSwimTime = timezone.now() - result.res_StartSwimTime)
            break
        if case(SP_TR1):
            results.update(res_StartCicleTime = timezone.now() - result.res_StartSwimTime)
            break
        if case(SP_CICLE):
            results.update(res_EndCicleTime = timezone.now() - result.res_StartSwimTime)
            break
        if case(SP_TR2):
            results.update(res_StartRunTime = timezone.now() - result.res_StartSwimTime)
            break
        if case(SP_RUN):
            results.update(res_EndRunTime = timezone.now() - result.res_StartSwimTime)
            break
        if case(SP_FINISHED):
            break
        print ("Not possible case. tapSportsman")
        break

    dbSaveAction(request.user, 2, str("sportsman_id={} sportsmanState={}").format(sportsman_id, sportsmanState))

    return redirect("../Results")


def tapStart(request):
    results = tblResults.objects
    results.update(res_StartSwimTime = timezone.now())
    results.update(res_EndSwimTime = None)
    results.update(res_StartCicleTime = None)
    results.update(res_EndCicleTime = None)
    results.update(res_StartRunTime = None)
    results.update(res_EndRunTime = None)

    dbSaveAction(request.user, 1, "Start")

    return redirect("./Results")


def GetResults(request):
    Results_list = tblResults.objects.all()
    Results_list = sorted(Results_list, reverse=True)

    current_user = request.user
    context = {'Results_list': Results_list}
    context['auth_user'] = current_user.is_authenticated()
    if current_user.is_authenticated():
        context['user'] = current_user.username
    else:
        context['user'] = 'anonymous'
    return render(request, 'index.html', context)


def GetTest(request):
    return render(request, 'test.html')


def GetLogin(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    return redirect("../Results")


def tapLogin(request):
    if not request.user.is_authenticated:
        username = request.GET['inputName']
        password = request.GET['inputPassword']
        user = authenticate(username=username, password=password)
        login(request, user)
    return redirect("../Results")




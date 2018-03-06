from django.conf import settings
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
#from django.db.models.functions import Coalesce

# Create your views here.
from django.http import HttpResponse
from .models import tbls24Results, tbls24ActionLog, tbls24Sportsman, tbls24Counter, tbls24Distance
from datetime import timedelta


FASTEST_LAP        = 5

ACT_LOGIN          = 100
ACT_LOGOUT         = 101
ACT_TAP_START      = 102
ACT_TAP_SPORTSMAN  = 103
ACT_TAP_SM_FINISH  = 104

class switch(object):
    value = None

    def __new__(class_, value):
        class_.value = value
        return True


def case(*args):
    return any((arg == switch.value for arg in args))


def index(request):
#    return render_template('signup.html')
    return HttpResponse("Hello, world. You're at the polls index.")


def dbSaveAction(user, action_id, action_desc):
    tbls24ActionLog.add(user, timezone.now(), action_id, action_desc)


def tapSportsman(request, sportsman_id):
    if not request.user.is_authenticated:
        return redirect("./s24Results")

    results = tbls24Results.objects.filter(res_Sportsman__exact=sportsman_id)
    result = results[0]

    if result.res_StartTime is None :
        results.update(res_StartTime = timezone.now(), res_LastLapTime = timezone.now())
    else:
        dt = result.res_LastLapTime
        if dt is not None and timezone.now() - dt > timedelta(seconds=FASTEST_LAP) :
            results.update(res_SwimLaps = result.res_SwimLaps + 1, res_LastLapTime = timezone.now())

    dbSaveAction(request.user, ACT_TAP_SPORTSMAN, str("sportsman_id={} SwimLaps={}").format(sportsman_id, result.res_SwimLaps))

    return redirect("../s24Results")


def tapSportsmanFinish(request, sportsman_id):
    if not request.user.is_authenticated:
        return redirect("./s24Results")

    results = tbls24Results.objects.filter(res_Sportsman__exact=sportsman_id)
    result = results[0]

    if result.res_StartTime is not None :
        results.update(res_FinishTime = timezone.now() - result.res_StartTime)

    dbSaveAction(request.user, ACT_TAP_SM_FINISH, str("sportsman_id={} SwimLaps={}").format(sportsman_id, result.res_SwimLaps))

    return redirect("../s24Results")



def tapStart(request, distance_id):
    if not request.user.is_authenticated:
        return redirect("../s24Results")

    sportsmen = [sm.cnt_Sportsman for sm in tbls24Counter.objects.filter(cnt_user=request.user)]

    start_time=timezone.now()
    for sm in sportsmen:
        if sm.sm_Distance.dst_Name == distance_id:
            tbls24Results.objects.filter(res_Sportsman=sm).delete()
            smresult = tbls24Results.objects.create(res_Sportsman=sm, res_StartTime = start_time, res_LastLapTime = start_time, res_SwimLaps = 0, res_FinishTime = None)
            smresult.save()

    dbSaveAction(request.user, ACT_TAP_START, str("Start {}").format(distance_id))

    return redirect("../s24Results")


def Gets24Results(request):
    current_user = request.user
    context = dict()

    if request.user.is_authenticated:
        sportsmen = [sm.cnt_Sportsman for sm in tbls24Counter.objects.filter(cnt_user=request.user)]
    else:
        sportsmen = [sm.cnt_Sportsman for sm in tbls24Counter.objects.all()]       

    distances = [dst.dst_Name for dst in tbls24Distance.objects.all()]
    context["distances"] = list(distances)
    dri_list = list()
    for dst in distances:
        dri = list()
        dri.append(dst)

        if request.user.is_authenticated:
            dst_sportsmen = [sm.cnt_Sportsman for sm in tbls24Counter.objects.filter(cnt_user=request.user, cnt_Sportsman__sm_Distance__dst_Name=dst)]
        else:
            dst_sportsmen = [sm.cnt_Sportsman for sm in tbls24Counter.objects.filter(cnt_Sportsman__sm_Distance__dst_Name=dst)]

        results_list = tbls24Results.objects.filter(res_Sportsman__in=dst_sportsmen)
        results_list = sorted(results_list, reverse=True)
        dri.append(results_list)
        dri_list.append(dri)

    context['dri_list'] = dri_list

    results_list = tbls24Results.objects.filter(res_Sportsman__in=sportsmen)
    results_list = sorted(results_list, reverse=True)

    context['Results_list'] = results_list
    context['auth_user'] = current_user.is_authenticated()

    if current_user.is_authenticated():
        context['user'] = current_user.username
    else:
        context['user'] = 'anonymous'

    print("Gets24Results - ", context)

    return render(request, 'S24Results.html', context)


def GetLogin(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    return redirect("../s24Results")


def tapLogin(request):
    if not request.user.is_authenticated:
        username = request.GET['inputName']
        password = request.GET['inputPassword']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
    return redirect("../s24Results")


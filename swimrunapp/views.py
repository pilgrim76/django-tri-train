from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse


def index(request):
#    Results_list = tblResults.objects.order_by('res_Sportsman')
#    context = {'Results_list': Results_list}
#    User = 
    context = {}
    return render(request, 'index.html', context)


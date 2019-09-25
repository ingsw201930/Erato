from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Client
from app_sw.models import Service
# Create your views here.
# Home for clients
@login_required
def home_c(request):
    user = request.user
    try:
        client=Client.objects.get(user=user)
    except:
        return HttpResponseRedirect('/')
    services=Service.objects.all()[:10]
    return render(request, 'home_c/home.html', {'client':client,'services':services})

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Models import
from app_sw.models import SW
from app_client.models import Client

# Main bifurcation, manu where user decides if using Erato as a client or sex worker.
def main_(request):
    return render_to_response('main/home.html')

def login_managing(request):
    render_ = None;
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    login(request, user)
    print("In sesssuibs")
    print(user)
    if user is not None:
        if SW.objects.filter(user=user):
            render_ = HttpResponseRedirect('/home/s/')
            return render_
        if Client.objects.filter(user=user):
            render_ = HttpResponseRedirect('/home/c/')
            return render_
    return render_

def logout_managing(request):
    logout(request)
    return HttpResponseRedirect('/')
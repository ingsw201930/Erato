from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from django.http import JsonResponse

# Models import
from app_sw.models import SW
from app_client.models import Client

# Main bifurcation, manu where user decides if using Erato as a client or sex worker.
def main_(request):
    return render(request, 'main/home.html', {'request': request})

def login_managing(request):
    render_ = None;
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        ## Aquí debería fallar bonito
        return HttpResponseRedirect('/')
    login(request, user)
    print(user)
    render_=HttpResponseRedirect('/')
    if user is not None:
        if SW.objects.filter(user=user):
            render_ = HttpResponseRedirect('/s/home/')
            return render_
        if Client.objects.filter(user=user):
            render_ = HttpResponseRedirect('/c/home/')
            return render_
    return render_

def user_exists(request):
    exists = False
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        exists = True
    data = {
        'exists': exists
    }
    return JsonResponse(data)

def logout_managing(request):
    logout(request)
    return HttpResponseRedirect('/')

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Models import
from app_sw.models import SW
from app_client.models import Client

# Main bifurcation, manu where user decides if using Erato as a client or sex worker.
def main_(request):
    return render(request, 'main/home.html', {'request': request})

@login_required
def login_managing(request):
    user = request.user
    print(user)
    render_= None
    if user is not None:
        if SW.objects.filter(user=user):
            render_ = HttpResponseRedirect('/s/home/')
            return render_
        if Client.objects.filter(user=user):
            render_ = HttpResponseRedirect('/c/home/')
            return render_
    return HttpResponseRedirect('/')

def user_exists(request):
    exists = False
    username = request.POST['username']
    password = request.POST['password']
    is_normal = False
    user = authenticate(username=username, password=password)
    if user is not None:
        exists = True
    if SW.objects.filter(user=user) or Client.objects.filter(user=user):
        is_normal = True
    print(is_normal)
    data = {
        'exists': exists,
        'is_normal': is_normal
    }
    return JsonResponse(data)

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    return JsonResponse({'authenticated':True})

def logout_managing(request):
    logout(request)
    return HttpResponseRedirect('/')

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientSignUpForm
from app_sw.models import Service
from app_date.models import Date
from django.contrib.auth import authenticate
from django.contrib.auth import login
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


def signup(request):
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            client=Client(
                user=user,
                birth_date=form.cleaned_data.get('birth_date'),
                email=form.cleaned_data.get('email')
            )
            client.save()
            login(request, user)
            return HttpResponseRedirect('/c/home/')
    else:
        form = ClientSignUpForm()
    return render(request, 'signup_c/signup_c.html', {'form': form})


# Me seeing my own profile 
@login_required
def my_profile(request):
    user = request.user
    try:
        client=Client.objects.get(user=user)
        return render(request, 'client/profile.html', {'client': client})
    except:
        print("Couldn't show public profile.")
    return HttpResponseRedirect('/')

@login_required
def dates(request):
    user = request.user
    client=Client.objects.get(user=user)
    dates = Date.objects.all().filter(client_id=client.user_id)
    accepted_dates=dates.filter(state='requested')
    requested_dates=dates.filter(state='requested')
    history_dates=dates
    return render(request, 'client/dates.html', {'accepted_dates':accepted_dates, 'requested_dates':requested_dates, 'history_dates':history_dates})
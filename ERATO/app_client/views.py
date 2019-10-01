from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientSignUpForm
from app_sw.models import Service
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
                birthDate=form.cleaned_data.get('birthDate')
            )
            client.save()
            login(request, user)
            return HttpResponseRedirect('/home/c/')
    else:
        form = ClientSignUpForm()
    return render(request, 'signup_c/signup_c.html', {'form': form})

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientSignUpForm
from .forms import UploadFileForm
from .forms import UploadMCForm
from app_sw.models import Service
from app_date.models import Date
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .decorators import login_required_client
# Create your views here.
# Home for clients


@login_required_client
def home_c(request):
    services=Service.objects.all()[:10]
    client=Client.objects.get(user=request.user)
    return render(request, 'home_c/home.html', {'client':client,'services':services})


@login_required_client
def get_service_list(request,index):
    n=5
    services=Service.objects.all()[index*n:(index+1)*n]
    return render(request,'home_c/services.html',{'services':services})

def signupform(request):
    form = ClientSignUpForm()
    form_ul = UploadFileForm()
    form_mc = UploadMCForm()
    return render(request, 'signup_c/signup_c.html', {'form': form, 'form_ul': form_ul, 'form_mc':form_mc})


def signup(request):
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        form_ul = UploadFileForm(request.POST, request.FILES)
        if form.is_valid() and request.FILES['file']:
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            client=Client(
                user=user,
                email=form.cleaned_data.get('email')
            )
            handle_uploaded_file(request.FILES['file'], username)
            client.save()
            login(request, user)
            return HttpResponseRedirect('/c/home/')
    else:
        form = ClientSignUpForm()
    return render(request, 'signup_c/signup_c.html', {'form': form})

def handle_uploaded_file(f, username):
    file_name = "assets/images/pro_pics/%s.png" % hash(username+erato_key)
    file_name = "assets/images/pro_pics/%s" % hashlib.md5((username+erato_key).encode()).hexdigest()
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Me seeing my own profile
@login_required_client
def my_profile(request):
    user = request.user
    client=Client.objects.get(user=user)
    return render(request, 'client/profile.html', {'client': client})

@login_required_client
def dates(request):
    user = request.user
    client=Client.objects.get(user=user)
    dates = Date.objects.all().filter(client_id=client.user_id)
    accepted_dates=dates.filter(state=Date.ACCEPTED)
    requested_dates=dates.filter(state=Date.REQUESTED)
    history_dates=dates
    return render(request, 'client/dates.html', {'accepted_dates':accepted_dates, 'requested_dates':requested_dates, 'history_dates':history_dates})

@login_required_client
def get_date_list(request,index):
    n=5
    user = request.user
    client=Client.objects.get(user=user)
    dates = Date.objects.filter(client=client)[index*n:(index+1)*n]
    return render(request, 'sw/date_list.html',{"dates":dates})

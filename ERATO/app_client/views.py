from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientSignUpForm
from .forms import UploadFileForm
from .forms import UploadMCForm
from .forms import FilterForm
from app_sw.models import Service
from app_date.models import Date
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .decorators import login_required_client
import hashlib
from ERATO.settings import BASE_DIR
from django.db.models import Q
# Create your views here.
# Home for clients
image_key= "Uribeparaco"
mc_key= "Conan"

@login_required_client
def home_c(request):
    services=Service.objects.all()[:10]
    client=Client.objects.get(user=request.user)
    form=FilterForm()
    return render(request, 'home_c/home.html', {'client':client,'services':services,'form':form})


@login_required_client
def get_service_list(request,index):
    n=6
    #name description filtering
    search=request.GET.get("search",None)
    query=Q(description__icontains=search)
    query|=Q(name__icontains=search)
    #sw filtering
    username=request.GET.get("user",None)
    query&=Q(sw__user__username__icontains=username)
    #weight filtering
    weight_min=request.GET.get("weight_min",None)
    weight_max=request.GET.get("weight_max",None)
    if weight_min!=None and weight_max!=None:
        weight_min=int(weight_min)
        weight_max=int(weight_max)
        query&=Q(sw__appearance__weight__gte=weight_min,sw__appearance__weight__lte=weight_max)
    #height filtering
    height_min=request.GET.get("height_min",None)
    height_max=request.GET.get("height_max",None)
    if height_min!=None and height_max!=None:
        height_min=float(height_min)
        height_max=float(height_max)
        query&=Q(sw__appearance__height__gte=height_min,sw__appearance__height__lte=height_max)
    price_min=request.GET.get("price_min",None)
    price_max=request.GET.get("price_max",None)
    if price_min!=None and price_max!=None:
        price_min=float(price_min)
        price_max=float(price_max)
        query&=Q(price__gte=price_min,price__lte=price_max)
    services=Service.objects.filter(query)[index*n:(index+1)*n]
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
        print(form.errors)
        if form.is_valid() and request.FILES['file']:
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            client=Client(
                user=user,
                birth_date=form.cleaned_data.get('birth_date'),
                email=form.cleaned_data.get('email'),
                picture_path = "%s" % hashlib.md5((username+image_key).encode()).hexdigest(),
                mc_path = "%s" % hashlib.md5((username+mc_key).encode()).hexdigest(),
            )
            handle_uploaded_file(request.FILES['file'], username, "PPC")
            handle_uploaded_file(request.FILES['file'], username, "MC")
            client.save()
            login(request, user)
            return HttpResponseRedirect('/c/home/')
    else:
        form = ClientSignUpForm()
    return render(request, 'signup_c/signup_c.html', {'form': form})

def handle_uploaded_file(f, username, code):
    file_name=''
    if code == 'PPC':
        file_name = BASE_DIR+"/assets/images/pro_pics/%s" % hashlib.md5((username+image_key).encode()).hexdigest()
    if code == 'MC':
        file_name =BASE_DIR+ "/assets/mcs/%s" % hashlib.md5((username+mc_key).encode()).hexdigest()
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Me seeing my own profile
@login_required_client
def my_profile(request):
    user = request.user
    client=Client.objects.get(user=user)
    return render(request, 'client/profile.html', {'client': client})

# Me seeing my own profile
@login_required_client
def edit_profile(request):
    user = request.user
    client=Client.objects.get(user=user)
    if request.method == 'POST':
        form = ClientEditForm(request.POST)
        if form.is_valid():
            print("Valid form")
            # weight = form.cleaned_data['weight']
    return HttpResponseRedirect('/s/profile/')


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

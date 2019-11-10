from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import SW,Service,Tag
from app_date.models import Date
from .forms import SWSignUpForm
from .forms import SWEditForm
from .forms import UploadFileForm
from .forms import UploadMCForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .decorators import *
from app_client.decorators import *
import hashlib
from ERATO.settings import BASE_DIR

from app_sw.forms import ServiceAddForm


erato_key= "er"

# Create your views here.
# Home for sexworkers
@login_required_SW
def home_s(request):
    user = request.user
    if user.is_authenticated:
        try:
            sw = SW.objects.get(user=user)
        except:
            return HttpResponseRedirect('/')
        return render(request, 'home_s/home.html', {'sw':sw, 'profile_pic':hash(user.username+erato_key)})
    else:
        HttpResponseRedirect('/')

@login_required_SW
def service_add_form(request):
    form = ServiceAddForm()
    tags = Tag.objects.all()
    return render(request, 'services_s/service_add.html', {'tags':tags,'form':form})

@login_required_SW
def service_add(request):
    form = ServiceAddForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        description = form.cleaned_data.get('description')
        price = form.cleaned_data.get('price')
        tags = form.cleaned_data.get('tags')
        user = request.user
        sw = SW.objects.get(user=user)
        service = Service(sw=sw, name=name, description=description, price=price)
        service.save()
        for tag in tags:
            service.tags.add(tag)
            service.save()

        return HttpResponseRedirect('/s/home')
    return HttpResponseRedirect('/s/service_add_request/')

@SW_my_service_required
def service_del(request, service_id):
    Service.objects.filter(id=service_id).delete()
    return HttpResponse("Borrando servicio")

def signupform(request):
    form = SWSignUpForm()
    form_ul = UploadFileForm()
    form_mc = UploadMCForm()
    return render(request, 'signup_s/signup_s.html', {'form': form, 'form_ul': form_ul, 'form_mc' : form_mc})

def signup(request):
    if request.method == 'POST':
        form = SWSignUpForm(request.POST)
        form_ul = UploadFileForm(request.POST, request.FILES)
        form_mc = UploadMCForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid() and request.FILES['file'] and request.FILES['mc']:
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username, email, raw_password)
            user.save()
            sw=SW(
                user=user,
                birth_date=form.cleaned_data.get('birth_date'),
                about=form.cleaned_data.get('description'),
                third_email=form.cleaned_data.get('third_email'),
                picture_path = BASE_DIR+"/assets/images/pro_pics/%s" % hashlib.md5((username+erato_key).encode()).hexdigest(),
                MC_path=BASE_DIR+"/assets/mcs/%s" % hashlib.md5((username).encode()).hexdigest(),
                gender=form.cleaned_data.get('gender'),
            )
            sw.save()
            handle_uploaded_file(request.FILES['file'], username, 'PPSW')
            print(request.FILES['file'])
            print("Profile picture saved")
            handle_uploaded_file(request.FILES['mc'], username, 'MC')
            print(request.FILES['mc'])
            print("Medical certification saved")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/s/home/')
        else:
            return render(request, 'signup_s/signup_s.html', {'form': form, 'form_ul': form_ul, 'form_mc': form_mc})
    return HttpResponseRedirect('/')

def handle_uploaded_file(f, username, code):
    file_name=''
    if code == 'PPSW':
        file_name = BASE_DIR+"/assets/images/pro_pics/%s" % hashlib.md5((username+erato_key).encode()).hexdigest()
    if code == 'MC':
        file_name =BASE_DIR+ "/assets/mcs/%s" % hashlib.md5((username+erato_key).encode()).hexdigest()
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def public_profile(request, sw_id):
    temp=sw_id
    print(temp)
    services=Service.objects.all()
    print("Showing services")
    print(services)
    sw=SW.objects.get(user_id=sw_id)
    return render(request, 'c/profiles/profile_s.html', {'sw': sw})

    print("Couldn't show public profile.")
    return None

@login_required_SW
def dates(request):
    user = request.user
    dates = Date.objects.filter(service__sw_id=user.id)
    non_rated_dates = dates.filter(state=Date.ENDED)
    current_date = dates.filter(state=Date.STARTED)
    requested_dates = dates.filter(state=Date.REQUESTED)
    all_dates = dates.filter(state=Date.RATED)
    return render(request, 'sw/dates.html', {'current_dates' : current_date, 'non_rated_dates': non_rated_dates, 'requested_dates' : requested_dates, 'all_dates' : all_dates})

@login_required_SW
def get_date_list(request,index):
    n=5
    user = request.user
    dates = Date.objects.filter(service__sw_id=user.id)
    non_rated_dates = dates.filter(state=Date.ENDED)[index*n:(index+1)*n]
    return render(request, 'sw/date_list.html',{'non_rated_dates' : non_rated_dates})

@login_required
def view_service(request, service_id):
    service = Service.objects.get(id=service_id)
    sw = service.sw
    return render(request, 'services_s/service_view.html', {'service':service, 'sw':sw})

@login_required_SW
def my_profile(request):
    form = SWEditForm()
    user = request.user
    sw = SW.objects.get(user=user)
    services = Service.objects.filter(sw_id=sw.user_id)
    return render(request, 'sw/profile.html', {'form':form, 'sw':sw, 'services':services})

@login_required_SW
def edit_profile(request):
    if request.method == 'POST':
        form = SWEditForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
    return HttpResponseRedirect('/s/profile/')

def history(request):
    return render(request, 'sw/history.html', {})

def payments(request):
    return render(request, 'sw/pay.html', {})

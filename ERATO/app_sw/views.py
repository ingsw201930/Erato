from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Models
from .models import SW,Service,Tag, Appearance
from app_date.models import Date
from app_mc.models import MC

# Forms
from .forms import SWSignUpForm
from .forms import SWEditForm
from .forms import UploadFileForm
from .forms import UploadMCForm
from .forms import ServiceAddForm
from .forms import SWAppearanceForm

# Authentication
from django.contrib.auth import authenticate
from django.contrib.auth import login

# Decorators
from .decorators import *
from app_client.decorators import *

from ERATO.settings import BASE_DIR

import hashlib
from time import gmtime, strftime

image_key="Conan"
mc_key="Conan"

fmt = '%Y-%m-%d %H:%M:%S+00:00'

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
        return render(request, 'home_s/home.html', {'sw':sw})
    else:
        HttpResponseRedirect('/')

@login_required_SW
def service_add_form(request):
    form = ServiceAddForm()
    tags = Tag.objects.all()
    return render(request, 'services_s/service_add.html', {'tags':tags, 'form':form})

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
    form_appearance = SW
    form_ul = UploadFileForm()
    form_mc = UploadMCForm()
    form_ap = SWAppearanceForm()
    return render(request, 'signup_s/signup_s.html', {'form_ap':form_ap,  'form': form, 'form_ul': form_ul, 'form_mc' : form_mc})

def signup(request):
    if request.method == 'POST':
        form = SWSignUpForm(request.POST)
        form_ul = UploadFileForm(request.POST, request.FILES)
        form_mc = UploadMCForm(request.POST, request.FILES)
        form_ap = SWAppearanceForm(request.POST)
        print(form_ap.errors)
        if form.is_valid() and form_ap.is_valid() and request.FILES['file'] and request.FILES['mc']:
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username, email, raw_password)

            mc_path = "%s" % hashlib.md5((username+mc_key).encode()).hexdigest(),
            mc=MC(
                file_path=mc_path,
                last_date=strftime(fmt, gmtime())
            )
            mc.save()

            sw=SW(
                user=user,
                mc=mc,
                full_name=form.cleaned_data.get('first_name')+' '+form.cleaned_data.get('last_name'),
                birth_date=form.cleaned_data.get('birth_date'),
                about=form.cleaned_data.get('description'),
                third_email=form.cleaned_data.get('third_email'),
                picture_path = "%s" % hashlib.md5((username+image_key).encode()).hexdigest(),
                gender=form.cleaned_data.get('gender'),
            )



            appearance = Appearance(
                sw=sw,
                weight=form_ap.cleaned_data.get('weight'),
                height=form_ap.cleaned_data.get('height'),
                eyes=form_ap.cleaned_data.get('eyes'),
                skin=form_ap.cleaned_data.get('skin'),
                hair_color=form_ap.cleaned_data.get('hair_color'),
                hair_style=form_ap.cleaned_data.get('hair_style'),
            )

            user.save()
            sw.save()
            appearance.save()

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
        file_name = BASE_DIR+"/assets/images/pro_pics/%s" % hashlib.md5((username+image_key).encode()).hexdigest()
    if code == 'MC':
        file_name =BASE_DIR+ "/assets/mcs/%s" % hashlib.md5((username+mc_key).encode()).hexdigest()
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
    current_date = dates.filter(state=Date.STARTED) | dates.filter(state=Date.TIMEDOUT)
    requested_dates = dates.filter(state=Date.REQUESTED)
    payed_dates = dates.filter(state=Date.PAYED)
    all_dates = dates.filter(state=Date.RATED) | dates.filter(state=Date.ENDED) | dates.filter(state=Date.REJECTED) | dates.filter(state=Date.ACCEPTED)
    return render(request, 'sw/dates.html', {'current_dates' : current_date, 'requested_dates' : requested_dates, 'payed_dates' : payed_dates, 'all_dates' : all_dates})

@login_required_SW
def get_date_list_more_dates(request, index):
    n=5
    user = request.user
    dates = Date.objects.filter(service__sw_id=user.id)
    all_dates = dates.filter(state=Date.RATED) | dates.filter(state=Date.ENDED) | dates.filter(state=Date.REJECTED) | dates.filter(state=Date.ACCEPTED)
    all_dates = all_dates[index*n:(index+1)*n]
    return render(request, 'sw/date_list.html', {'all_dates' : all_dates})

@login_required
def view_service(request, service_id):
    service = Service.objects.get(id=service_id)
    sw = service.sw
    return render(request, 'services_s/service_view.html', {'service':service, 'sw':sw})

@login_required_SW
def my_profile(request):
    form = SWEditForm()
    form_ul = UploadFileForm()
    form_mc = UploadMCForm()
    form_ap = SWAppearanceForm()
    user = request.user
    sw = SW.objects.get(user=user)
    ap = Appearance.objects.get(sw_id=sw.user_id)
    services = Service.objects.filter(sw_id=sw.user_id)
    return render(request, 'sw/profile.html', {'form_ul': form_ul, 'form_mc': form_mc, 'form_ap':form_ap,  'form':form, 'sw':sw, 'ap':ap, 'services':services})

@login_required_SW
def account_del(request, sw_id):
    user = request.user
    sw = SW.objects.get(user=user)
    sw.delete()
    user.delete()
    return HttpResponseRedirect('/')

@login_required_SW
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        form = SWEditForm(request.POST)
        form_ap = SWAppearanceForm(request.POST)
        if form.is_valid() and form_ap.is_valid():
            sw = SW.objects.get(user=user)
            ap = Appearance.objects.get(sw_id=sw.user_id)

            sw.gender = form.cleaned_data['gender']
            sw.third_email = form.cleaned_data['third_email']
            sw.about = form.cleaned_data['about']

            ap.weight = form_ap.cleaned_data['weight']
            ap.height = form_ap.cleaned_data['height']
            ap.eyes = form_ap.cleaned_data['eyes']
            ap.hair_style = form_ap.cleaned_data['hair_style']
            ap.hair_color = form_ap.cleaned_data['hair_color']

            sw.save()
            ap.save()

    return HttpResponseRedirect('/s/profile/')

def upload_swpp(request):
    user = request.user
    username =str(user)
    if request.FILES['file']:
        handle_uploaded_file(request.FILES['file'], username, 'PPSW')
    return HttpResponseRedirect('/s/profile/')

@login_required_SW
def mc_panel(request):
    form_mc = UploadMCForm()
    return render(request, 'sw/mc_panel.html', {'form_mc':form_mc})

def update_mc(request):

    return HttpResponse("Updating")

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import SW,Service
from app_date.models import Date
from .forms import SWSignUpForm
from .forms import UploadFileForm
from django.contrib.auth import authenticate
from django.contrib.auth import login


from app_sw.forms import ServiceAddForm


erato_key= "er"
# Create your views here.
# Home for sexworkers
@login_required
def home_s(request):
    user = request.user
    print("In users")
    print(user)
    if user.is_authenticated:
        try:
            sw = SW.objects.get(user=user)
        except:
            return HttpResponseRedirect('/')
        return render(request, 'home_s/home.html', {'sw':sw, 'profile_pic':hash(user.username+erato_key)})
    else:
        HttpResponseRedirect('/')

@login_required
def service_add_form(request):
    form = ServiceAddForm();
    return render(request, 'services_s/service_add.html', {'form':form})

@login_required
def service_add(request):
    form = ServiceAddForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        description = form.cleaned_data.get('description')
        price = form.cleaned_data.get('price')
        user = request.user
        try :
            sw = SW.objects.get(user=user)
        except:
            return HttpResponse('El usuario es invalido')
        service = Service(sw=sw, name=name, description=description, price=price)
        service.save()
        return HttpResponseRedirect('/s/home')

@login_required
def service_del(request, service_id):
    Service.objects.filter(id=id).delete()
    return HttpResponse("Borrando servicio")

@login_required
def service_edit_form(request, service_id):
     return HttpResponse("Editando servicio")


def signup(request):
    if request.method == 'POST':
        form_ul = UploadFileForm(request.POST, request.FILES)
        form = SWSignUpForm(request.POST)
        if form.is_valid() and form_ul.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            sw=SW(
                user=user,
                birth_date=form.cleaned_data.get('birthDate'),
                about=form.cleaned_data.get('description'),
                third_email=form.cleaned_data.get('third_email'),
                picture_path = "assets/images/pro_pics/%s" % hash(username+erato_key),
                MC_path="media/%s" % hash(username+erato_key)
            )
            handle_uploaded_file(request.FILES['file'], username)
            sw.save()
            login(request, user)

            return HttpResponseRedirect('/s/home/')
    else:
        form = SWSignUpForm()
        form_ul = UploadFileForm()
        return render(request, 'signup_s/signup_s.html', {'form': form, 'form_ul': form_ul})
    #Página de registro
    return HttpResponseRedirect('/s/home/')

def handle_uploaded_file(f, username):
    file_name = "assets/images/pro_pics/%s.png" % hash(username+erato_key)
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

@login_required
def pending_dates(request):
    user = request.user
    sw = SW.objects.get(user=user)
    services = Service.objects.filter(sw_id=sw.user_id)
    dates = []
    for service in services:
        dates = Date.objects.filter(service_id=service.id)
        # dates = dates.filter(state='started')
    return render(request, 'pending_dates/pending_dates.html', {'dates' : dates})

def view_service(request, service_id):
    service = Service.objects.get(id=service_id)
    return render(request, 'services_s/service_view.html', {'service':service})

def my_profile(request):
    return render(request, 'profiles/profile_s_edit.html', {})

def history(request):
    return render(request, 'services_s/history.html', {})

def payments(request):
    return render(request, 'payments/pay.html', {})
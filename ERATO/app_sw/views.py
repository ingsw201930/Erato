from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import SW,Service
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
        return HttpResponseRedirect('/home/s')

@login_required
def service_del(request, service_id):
     return HttpResponse("Borrando servicio")

@login_required
def service_edit_form(request, service_id):
     return HttpResponse("Editando servicio")


def signup(request):
    if request.method == 'POST':

        form = SWSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            sw=SW(
                user=user,
                birthDate=form.cleaned_data.get('birthDate'),
                about=form.cleaned_data.get('description'),
                third_email=form.cleaned_data.get('third_email'),
                MC_path="media/%s" % hash(username+erato_key)
            )
            sw.save()
            login(request, user)
            form_ul = UploadFileForm(request.POST, request.FILES)
            if form_ul.is_valid():
                handle_uploaded_file(request.FILES['file'], username)
                return HttpResponseRedirect('/home/s/')

    else:
        form = SWSignUpForm()
        form_ul = UploadFileForm()
    return render(request, 'signup_s/signup_s.html', {'form': form, 'form_ul': form_ul})

def handle_uploaded_file(f, username):
    file_name = "assets/images/pro_pics/%s" % hash(username+erato_key)
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
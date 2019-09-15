from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import SW,Service


from app_sw.forms import ServiceAddForm

# Create your views here.
# Home for sexworkers
@login_required
def home_s(request):
    user = request.user
    print("In users")
    print(user)
    if user.is_authenticated:
        sw = SW.objects.get(user=user)
        return render(request, 'home_s/home.html', {'sw':sw})
    else:
        HttpResponseRedirect('/')

@login_required
def service_add_form(request):
    form = ServiceAddForm();
    return render(request, 'services_s/service_add.html', {'form':form})

@login_required
def service_add(request):
    name = request.POST['name']
    description = request.POST['description']
    price = request.POST['price']

    user = request.user
    sw = SW.objects.get(user=user)

    service = Service(sw=sw, name=name, description=description, price=price)
    service.save()

    return HttpResponseRedirect('/home/s')

@login_required
def service_del(request):
    return HttpResponseRedirect('/')

@login_required
def service_edit_form(request):
    return HttpResponseRedirect('/')

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import SW,Service
from .forms import SWSignUpForm
from django.contrib.auth import authenticate
from django.contrib.auth import login


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
def service_del(request, service_id):
     return HttpResponse("Borrando servicio")

@login_required
<<<<<<< HEAD
def service_edit_form(request, service_id):
     return HttpResponse("Editando servicio")
=======
def service_edit_form(request):
    return HttpResponseRedirect('/')

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
                about=form.cleaned_data.get('description')
            )
            sw.save()
            login(request, user)
            return HttpResponseRedirect('/home/s/')
    else:
        form = SWSignUpForm()
    return render(request, 'signup_s/signup_s.html', {'form': form})
>>>>>>> d3aeffc552fd9c44093a4aba454e216e36dbb6c5

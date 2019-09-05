from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import SW
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
def login(request):
	mypath=os.path
	return render(request, "registration/login.html", {'path':mypath})
	#return render_to_response('ERATO/web/login.html')


#user_name is a parameter that comes from the url ex:home/gustavo ->username=gustavo
@login_required
def home_sw(request):
	mypath=os.path
	try:
		user=request.user
		sw=SW.objects.get(user=user)
	except User.DoesNotExist:
		raise Http404("Question does not exist")
	except SW.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, "home.html", {'sw':sw})

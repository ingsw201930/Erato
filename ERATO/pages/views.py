from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import SW
import os

# Create your views here.
def login(request):
	mypath=os.path
	return render(request, "registration/login.html", {'path':mypath})
	#return render_to_response('ERATO/web/login.html')

#user_name is a parameter that comes from the url ex:home/gustavo ->username=gustavo
def home_sw(request,user_name):
	mypath=os.path
	try:
		user=User.objects.get(username=user_name)#get user from U_N
		sw=SW.objects.get(user=user)
	except User.DoesNotExist:
		raise Http404("Question does not exist")
	except SW.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, "home.html", {'sw':sw})

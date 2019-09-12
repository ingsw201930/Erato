from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Client
from app_sw.models import Service
from django.contrib.auth.decorators import login_required
import os


#user_name is a parameter that comes from the url ex:home/gustavo ->username=gustavo
@login_required
def home_cl(request):
	mypath=os.path
	try:
		user=request.user
		cl=Client.objects.get(user=user)
	except User.DoesNotExist:
		raise Http404("User does not exist")
	except Client.DoesNotExist:
		raise Http404("SW does not exist")
	return render(request, "home_cl.html", {'cl':cl,'service_list':Service.objects.all()[:10]})

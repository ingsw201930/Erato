from django.http import HttpResponse
from django.shortcuts import render
import os

# Create your views here.
def login(request):
	mypath=os.path
	return render(request, "registration/login.html", {'path':mypath})
	#return render_to_response('ERATO/web/login.html')

def home_sw(request):
	mypath=os.path
	return render(request, "home.html", {'path':mypath})

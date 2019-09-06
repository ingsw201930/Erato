from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
def login(request):
	mypath=os.path
	return render(request, "registration/login.html", {'path':mypath})
	#return render_to_response('ERATO/web/login.html')

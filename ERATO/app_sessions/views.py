from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from app_sw.models import SW
from app_client.models import Client
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
def login(request):
	mypath=os.path
	return render(request, "registration/login.html", {'path':mypath})
	#return render_to_response('ERATO/web/login.html')

#this function checks if the user is a sw or cl and redirects acordingly
@login_required
def redirect_login(request):
	try:
		user=request.user
		cl=Client.objects.get(user=user)
	except User.DoesNotExist:
		raise Http404("User does not exist")
	except Client.DoesNotExist:
		cl=None
	if cl is None:
		try:
			sw=SW.objects.get(user=user)
		except SW.DoesNotExist:
			raise Http404("nor SW nor Client")#this can be better than 404
		return HttpResponseRedirect('/sw/home/')
	else:
		return HttpResponseRedirect('/cl/home/')

from django.contrib.auth.decorators import login_required
from .models import Client
from app_date.models import Date
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from functools import wraps

def login_required_client(view):
    @wraps(view)
    @login_required
    def wrap(*args,**kwargs):
        user = args[0].user
        try:
            client=Client.objects.get(user=user)
        except:
            return HttpResponseForbidden()
        return view(*args,**kwargs)
    return wrap

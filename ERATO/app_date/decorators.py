from .models import Date
from django.http import HttpResponseForbidden
from functools import wraps
from app_sw.decorators import login_required_SW
from app_client.decorators import login_required_client

def SW_my_date_required(view):
    @wraps(view)
    @login_required_SW
    def wrap(*args,**kwargs):
        user=args[0].user
        try:
            date=Date.objects.get(id=kwargs['date_id'])
        except:
            return HttpResponseForbidden()
        if user.username==date.service.sw.user.username:
            return view(*args,**kwargs)
        else:
            return HttpResponseForbidden()
    return wrap


def client_my_date_required(view):
    @wraps(view)
    @login_required_client
    def wrap(*args,**kwargs):
        user=args[0].user
        try:
            date=Date.objects.get(id=kwargs['date_id'])
        except:
            return HttpResponseForbidden()
        if user.username==date.client.user.username:
            return view(*args,**kwargs)
        else:
            return HttpResponseForbidden()
    return wrap
from django.contrib.auth.decorators import login_required
from .models import SW,Service
from app_date.models import Date
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from functools import wraps

def login_required_SW(view):
    @wraps(view)
    @login_required
    def wrap(*args,**kwargs):
        user = args[0].user
        try:
            sw=SW.objects.get(user=user)
        except:
            return HttpResponseForbidden()
        return view(*args,**kwargs)
    return wrap

#the parameters must be at least request,service_id
def SW_my_service_required(view):
    @wraps(view)
    @login_required_SW
    def wrap(*args,**kwargs):
        user=args[0].user
        try:
            service=Service.objects.get(id=kwargs['service_id'])
        except:
            return HttpResponseForbidden()
        if user.username==service.sw.user.username:
            return view(*args,**kwargs)
        else:
            return HttpResponseForbidden()
    return wrap

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
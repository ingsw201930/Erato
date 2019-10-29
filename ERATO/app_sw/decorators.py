from django.contrib.auth.decorators import login_required
from .models import SW,Service
from django.http import  HttpResponseForbidden
from functools import wraps

def login_required_SW(view):
    @wraps(view)
    @login_required
    def wrap(*args,**kwargs):
        user = args[0].user
        try:
            sw=SW.objects.get(user=user)
            print(sw.user.username)
        except Exception:
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
        except Exception:
            return HttpResponseForbidden()
        if user.username==service.sw.user.username:
            return view(*args,**kwargs)
        else:
            return HttpResponseForbidden()
    return wrap


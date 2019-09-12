from django.http import HttpResponse
from django.shortcuts import render
from .models import Date
from .QR import *

# Create your views here.

def createQR(request,date_id):
    generateQR(str(date_id))
    #enviar codigo qr
    #borrar codigo qr (assets/QR/<date_id>.svg)
    return HttpResponse("esto deberia redirigir a una pagina donde se envia el qr")

def checkQR(request,code):
    id=int(decode(secretkey,code))
    try:
        date=Date.objects.get(id=id)
    except Date.DoesNotExist:
        raise Http404("invalid QR")
    state=date.state
    if state=='payed':
        date.state='started'
        date.save()
    #send mail to third party
    responses={
        'pre-pay':'este date no ha sido pagado aun',
        'payed':'el codigo QR fue escaneado con exito, COMENZO EL SERVICIO!',
        'started':'este codigo qr ya fue usado con exito',
        'ended':'este date ya termino',
        'timedout':'este servicio ya quedo sin tiempo'
    }
    return HttpResponse(responses[state])#esto deberia ser una pagina bien hecha

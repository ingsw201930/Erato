from django.shortcuts import render
from .QR import generateQR
from .models import Date
from app_emails.utils import send_qr
from django.http import HttpResponse, HttpResponseRedirect
import os
from django.contrib.auth.decorators import login_required
from app_sw.models import Service
from .forms import DateAddForm
import logging
import threading
import time

from app_client.models import Client
# Create your views here.
def send_email(id, email):
    url = generateQR(id)
    path=os.path.join(os.getcwd()+'/assets/QR/'+id+'.svg')
    send_qr(path, email)

def createQR(request,date_id):
    generateQR(str(date_id))
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
        'payed':'el codigo QR fue escaneado con exito, COMENZÓ EL SERVICIO!',
        'started':'este codigo qr ya fue usado con exito',
        'ended':'este date ya termino',
        'timedout':'este servicio ya quedo sin tiempo'
    }
    return HttpResponse(responses[state])#esto deberia ser una pagina bien hecha

@login_required
def generate_date(request, service_id):
    form = DateAddForm( request.POST )

    if form.is_valid():

        start_time = form.cleaned_data.get('start_time')
        finish_time = form.cleaned_data.get('finish_time')
        place = form.cleaned_data.get('place')

        try:
            user = request.user
            service = Service.objects.get(id=service_id)
            client = Client.objects.get( user = user )

            date = Date(
                client = client,
                service = service,
                start = start_time,
                end = finish_time,
                place = place
            )
            date.save()
            send = "La cita ha sido creada."
        except Exception as e:

            send = str(e)
    else :
        return HttpResponseRedirect('/date_form/'+str(service_id))

    return HttpResponseRedirect( '/home/c' )

@login_required
def date_form( request , service_id ):
    form=DateAddForm()
    service = Service.objects.get( id = service_id )
    return render( request, 'date/date_form.html' , {'service':service,'form':form } )


@login_required
def date_by_service(request, service_id):
    return HttpResponse("Aqui se muestran las peticiones de date para: servicio "+str(service_id))

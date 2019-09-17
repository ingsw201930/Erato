from django.shortcuts import render
from .QR import generateQR
from .models import Date
from app_emails.utils import send_qr
from django.http import HttpResponse
import os
from django.contrib.auth.decorators import login_required
from app_sw.models import Service

from app_client.models import Client
# Create your views here.
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

def generate_date(request, service_id):

    user = request.user
    client = Client.objects.get(user=user)
    id = "myid1"
    #date = Date(client = client, service=service_id, start='00:00:00', end='00:00:00', place="Fuego blanco", state='pre-pay')
    #date.save()
    #url = generateQR(date.id)
    # id= date.id

    url = generateQR(id)
    path=os.path.join(os.getcwd()+'/assets/QR/'+id+'.svg')
    send_qr(path, 'ruastabi@gmail.com')
    return HttpResponse("Enviado")

@login_required
def date_form( request , service_id ):

    service = Service.objects.get( id = service_id )
    return render( request, 'date/date_form.html' , {'service':service } )

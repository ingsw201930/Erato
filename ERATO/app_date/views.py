from django.shortcuts import render
from .QR import generateQR,decode,secretkey
from .models import Date
from app_emails.utils import send_qr
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
import os
from django.contrib.auth.decorators import login_required
from app_sw.models import Service
from .forms import DateAddForm
import logging
import threading
import time
import random
from django.db.models import Q
from app_client.models import Client

# Create your views here.
def send_email(id, email):
    url = generateQR(id)
    path=os.path.join(os.getcwd()+'/assets/QR/'+id+'.svg')
    send_qr(path, email)

@login_required
def createQR(request,date_id):
    try:
        date=Date.objects.get(id=date_id)
    except Exception as e:
        return HttpResponse("date DoesNotExist")
    if date.state!=Date.PAYED:
        return HttpResponse("invalid date")
    if date.client.user.username==request.user.username:
        print("Valid user")
        noise=random.randrange(100000)
        date.noise=noise
        date.save()
        print("Before thread")
        def create_and_send():
            print("Creating QR and sending in thread")
            qr=generateQR(str(date_id),str(noise),request)
            client = Client.objects.get(user_id=date.client_id)
            email= client.email
            print("Sending QR to... %s with the id %d" % (email, client.id))
            send_qr(qr, email)

        thr = threading.Thread(target=create_and_send)
        thr.start()
        return HttpResponse("QR sent")
    else:
        return HttpResponseForbidden()

def checkQR(request,id,code):
    try:
        date=Date.objects.get(id=id)
    except Date.DoesNotExist:
        raise Http404("invalid QR")
    state=date.state
    noise=date.noise
    if state=='payed' and code==str(hash(str(id)+str(noise))):
        date.state='started'
        date.save()
    #send mail to third party
    responses={
        'pre-pay':'este date no ha sido pagado aun',
        'payed':'el codigo QR no funcionó!',
        'started':'COMENZO',
        'ended':'este date ya termino',
        'timedout':'este servicio ya quedo sin tiempo'
    }
    return HttpResponse(responses[state])#esto deberia ser una pagina bien hecha

@login_required
def generate_date(request, service_id):
    print("Generating date...")
    if request.method == 'POST':
        form = DateAddForm( request.POST )
        if form.is_valid():
            print("Form is valid")
            start_time = form.cleaned_data.get('start_time')
            print(start_time)
            end_time = form.cleaned_data.get('end_time')
            print(end_time)
            start_time_hms = form.cleaned_data.get('start_time_hms')
            print(start_time_hms)
            end_time_hms = form.cleaned_data.get('end_time_hms')
            print(end_time_hms)
            lng = round(form.cleaned_data.get('lng'),8)
            print(lng)
            lat = round(form.cleaned_data.get('lat'),8)
            print(lat)

            try:
                user = request.user
                service = Service.objects.get(id=service_id)
                client = Client.objects.get( user = user )
                date = Date(
                    client = client,
                    service = service,
                    start_time = start_time+' '+start_time_hms,
                    end_time = end_time+' '+end_time_hms,
                    lat = lat,
                    lng = lng
                )
                print("Creating date...")
                date.save()


                print("Date created")

                return HttpResponseRedirect('/c/home/')

            except Exception as e:
                print(e.args)
        else:
            form=DateAddForm()
    return HttpResponse("We couldn't generate date")


@login_required
def date_form( request , service_id ):
    form=DateAddForm()
    service = Service.objects.get( id = service_id )
    return render( request, 'date/date_form.html' , {'service':service,'form':form } )

@login_required
def accept_date(request, date_id):
    return HttpResponse("aqui se acepta el date")

@login_required
def date_by_service(request, service_id):
    try:
        service=Service.objects.get(id=service_id)
    except:
        return HttpResponse('servicio invalido')
    if service.sw.user.username!=request.user.username:
        return HttpResponseForbidden()
    query = Q(state=Date.REQUESTED)
    query.add(Q(state=Date.ACCEPTED), Q.OR)
    query.add(Q(state=Date.PAYED), Q.OR)
    dates=service.date_set.filter(query)
    return render(request, 'date_by_service/dates.html', {'service':service,'dates':dates})

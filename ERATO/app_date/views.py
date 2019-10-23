from django.shortcuts import render
from .QR import generateQR,decode,secretkey
from .models import Date
from app_emails.utils import send_qr
from app_emails.utils import send_third
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from app_sw.models import Service
from .forms import DateAddForm
import threading
import random
from django.db.models import Q
from app_client.models import Client
from app_sw.decorators import *
from .decorators import *
from datetime import datetime
import time
import hashlib

fmt = '%Y-%m-%d %H:%M:%S+00:00'

# Create your views here.

@client_my_date_required
def createQR(request,date_id):
    date=Date.objects.get(id=date_id)
    if date.state!=Date.PAYED:
        return HttpResponse("invalid date")
    print("Valid user")
    noise=random.randrange(100000)
    date.noise=noise
    date.save()
    print("Before thread")
    def create_and_send():
        print("Creating QR and sending in thread")
        qr=generateQR(str(date_id),str(noise),request)
        print(qr)
        client = Client.objects.get(user_id=date.client_id)
        email= client.email
        print("Sending QR to... %s with the id %d" % (email, client.user_id))
        send_qr(qr, email)

    thr = threading.Thread(target=create_and_send)
    thr.start()
    return HttpResponse("QR sent")

def checkQR(request,date_id,code):
    try:
        date=Date.objects.get(id=date_id)
    except Date.DoesNotExist:
        return HttpResponseForbidden()
    state=date.state
    noise=str(date.noise)
    code_noise = hashlib.sha256(bytes(str(date_id)+noise,'utf-8')).hexdigest()
    print("Code:"+code)
    print("Code + noise "+code_noise)
    print("noise,id",noise,date_id)
    if state==Date.PAYED and code==code_noise:
 #   if True:
        date.state=Date.STARTED
        date.save()
        state=Date.STARTED

        def date_timer():
            date_start  = datetime.strptime( str(date.start_time), fmt ).timestamp()
            date_end    = datetime.strptime( str(date.end_time)  , fmt ).timestamp()
            sleep_time =  date_end - date_start
            print("Sleeping %f" % sleep_time)
            time.sleep( sleep_time )
            if date.state != Date.ENDED:
                send_third( date.service.sw.user.username , date.service.sw.third_email )
                print( date.service.sw.third_email  )
                date.state = Date.TIMEDOUT
                date.save()

        thr = threading.Thread( target= date_timer )
        thr.start()

    #send mail to third party
    responses={
        Date.REQUESTED:'date_states/failed.html',
        Date.ACCEPTED:'date_states/failed.html',
        Date.PAYED:'date_states/failed.html',
        Date.STARTED:'date_states/started.html',
        Date.ENDED:'date_states/failed.html',
        Date.TIMEDOUT:'date_states/failed.html'
    }
    return render(request, responses[state], {})

@login_required_client
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
            user = request.user
            client = Client.objects.get( user = user )
            try:

                service = Service.objects.get(id=service_id)

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


@login_required_client
def date_form( request , service_id ):
    form=DateAddForm()
    service = Service.objects.get( id = service_id )
    return render( request, 'date/date_form.html' , {'service':service,'form':form } )

@SW_my_date_required
def accept_date(request, date_id):
    date=Date.objects.get(id=date_id)
    if date.state!=Date.REQUESTED:
        return HttpResponse('date invalido')
    date.state=Date.ACCEPTED
    date.save()
    return HttpResponse("aqui se acepta el date")

@SW_my_date_required
def reject_date(request, date_id):
    date=Date.objects.get(id=date_id)
    if date.state!=Date.REQUESTED:
        return HttpResponse('date invalido')
    date.state=Date.REJECTED
    date.save()
    return HttpResponse("aqui se acepta el date")


@SW_my_date_required
def end_date(request, date_id):
    date = Date.objects.get(id=date_id)
    date.state = 'ended'
    date.save()
    return HttpResponse("Date ended")

@SW_my_service_required
def date_by_service(request, service_id):
    service=Service.objects.get(id=service_id)
    query = Q(state=Date.REQUESTED)
    query.add(Q(state=Date.ACCEPTED), Q.OR)
    query.add(Q(state=Date.PAYED), Q.OR)
    dates=service.date_set.filter(query)
    return render(request, 'date_by_service/dates.html', {'service':service,'dates':dates})

@client_my_date_required
def pay_date(request,date_id):
    date=Date.objects.get(id=date_id)
    if date.state!=Date.ACCEPTED:
        return HttpResponse('date invalido')
    return render(request,'pay_date/pay_date.html',{'date_id':date_id})

@client_my_date_required
def pay_date_submit(request,date_id):
    date=Date.objects.get(id=date_id)
    if date.state!=Date.ACCEPTED:
        return HttpResponse('date invalido')
    #if payment is made
    date.state=Date.PAYED
    date.save()
    return HttpResponse('date is payed')

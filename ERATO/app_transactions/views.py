from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden,JsonResponse
from django.template.loader import render_to_string
import stripe

from app_transactions.models import Transaction
from datetime import datetime
import time

from .forms import TransactionForm

from app_client.decorators import login_required_client
from app_sw.decorators import login_required_SW
from app_date.models import Date

fmt = '%Y-%m-%d %H:%M:%S+00:00'

stripe.api_key = settings.STRIPE_SECRET_KEY


def charge(request, date_id):
	date = Date.objects.get(id=date_id)
	if date.state!=Date.ACCEPTED:
		return HttpResponse('Date invalido')
	if request.method == 'POST':
		transactionForm = TransactionForm(request.POST)
		print(transactionForm.errors)
		if transactionForm.is_valid():
			token = request.POST.get('stripeToken', False)
			now = datetime.now()
			current_time = now.strftime(fmt)
			print(current_time)
			transaction = Transaction(
				name = transactionForm.cleaned_data.get('name'),
				last_name=transactionForm.cleaned_data.get('last_name'),
				address=transactionForm.cleaned_data.get('address'),
				sw = date.service.sw,
				client = date.client,
				amount = date.price,
				date = current_time,
			)
			# Charge recibe un entero, pero las dos últimas cifras son centavos ._.
			price=int(round(date.price,0))*100

			print("Saving transaction")
			transaction.save()
			print("Transaction saved")
			print("Creando cargos")

			converted_price = int(price/3500)
			print("Transaction made, %d charged." % converted_price)
			stripe.Charge.create(
			amount = converted_price,
			currency='usd',
			card="tok_visa",
			description= str(date.id)+'_'+str(current_time)
			)
			print("Cuenta cobrada")
			transaction.state= transaction.ACCEPTED
			transaction.save()
			date.state=Date.PAYED
			date.save()

	return HttpResponseRedirect('/createqr/'+str(date_id))

@login_required_client
def c_payments(request):
	user = request.user
	transactions = Transaction.objects.filter(client_id=user.id)
	return render(request, 'client/payments.html', {'transactions':transactions})

@login_required_SW
def s_payments(request):
	user = request.user
	transactions = Transaction.objects.filter(sw_id=user.id)
	return render(request, 'sw/payments.html', {'transactions':transactions})

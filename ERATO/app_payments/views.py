from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden,JsonResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
def charge(request):
	#existing_order = get_order(request)
	publish_key = setting.STRIPE_PUBLISHABLE_KEY
	if request.method == 'POST':
		try:
			token = request.POST['stripeToken']
			charge = stripe.Charge.create(
				amount = 100,
				currency='cop',
				description='exampleCharge',
				source='token'
				)
		except stripe.CardError as e:
			message.info(request, "Your card has been declined")
	return HttpResponse('date is payed')
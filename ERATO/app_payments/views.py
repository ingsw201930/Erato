from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden,JsonResponse
import stripe
STRIPE_SECRET_KEY = 'pk_test_TJ2OVSToevGScWJgSpKiAhsm00lXDiVFap'
STRIPE_PUBLISHABLE_KEY = 'sk_test_5gjI6b94pzCgj1P31u9tQMXT00DXHdREmV'

stripe.api_key = STRIPE_SECRET_KEY
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
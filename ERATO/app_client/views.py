from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# Home for clients
@login_required
def home_c(request):
    user = request.user
    return render(request, 'home_c/home.html', {'client':user})

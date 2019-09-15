from django.shortcuts import render
from django.core.utils import send_mail

def index(request):
    send_mail(
    'Hello from ',
    ' ADSfhjk',
    'eratoservices@gmail.com',
    'xijilob@rev-mail.net'
    )

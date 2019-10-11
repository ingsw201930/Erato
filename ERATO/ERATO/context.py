

def baseurl(request):
    return {
        'BASEURL':'http://'+request.META['HTTP_HOST'],
    }



def baseurl(request):
    return {
        'BASEURL':request.META['HTTP_HOST'],
    }

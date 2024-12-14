from django.http import HttpResponseRedirect
from decouple import config


def admin_only_middleware(get_response):
    def middleware(request):
        allowed_ips = config('ALLOWED_IPS').split(',')

        if request.path.startswith('/admin') and request.META['REMOTE_ADDR'] not in allowed_ips:
            return HttpResponseRedirect('/no-access') 

        return get_response(request)

    return middleware

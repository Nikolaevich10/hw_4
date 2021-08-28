from django.utils import timezone

from ..models import Log


timestamp = timezone.now()


def wrap_log(get_response):

    def logging(request):
        if request.path.startswith('/admin') is False:
            Log.objects.create(path=request.path, timestamp=timestamp, method=request.method)

        response = get_response(request)
        return response

    return logging

from django.conf import settings
from django.core.urlresolvers import reverse
from logging import getLogger
from .models import Bib
import datetime
import json

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

class DumpRequestToLogMiddleware(object):
    def process_request(self, request):
        logger = getLogger('django.request')
        body = 'MULTIPART/FORMDATA'
        if 'CONTENT_TYPE' in request.META and request.META['CONTENT_TYPE'][:19] != 'multipart/form-data':
            body = request.body
        logger.debug(
            "[%s] Request is a %s, from %s, the path is %s, and body is %s" % (
            str(datetime.datetime.now()),
            request.method,
            request.META['REMOTE_ADDR'],
            request.path,
            body.decode('utf-8'))
        )
        return None

    def process_response(self, request, response):
        if request.path.startswith('/%s/' % settings.API_VERSION):
            body = 'MULTIPART/FORMDATA'
            if 'CONTENT_TYPE' in request.META and request.META['CONTENT_TYPE'][:19] != 'multipart/form-data':
                body = (request.body).decode('utf-8')
            if hasattr(response, 'content'):
                data = response.content
            if hasattr(response, 'data'):
                data = json.dumps(response.data, default=date_handler)
            Bib.objects.create(request_type=request.method, sent_at=str(datetime.datetime.now()), request_path=request.path, request_origin=request.META['REMOTE_ADDR'], request_body=body, response_code=response.status_code, response_data=data)
        return response
from django.db import models

class Bib(models.Model):
    request_type = models.CharField(max_length=255, blank=True, null=True)
    request_path = models.CharField(max_length=255, blank=True, null=True)
    sent_at = models.CharField(max_length=255, blank=True, null=True)
    request_body = models.TextField(blank=True, null=True)
    request_origin = models.CharField(max_length=255, blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    response_code = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return "[%s] Request is a %s from %s || PATH: %s || RESPONSE STATUS CODE: %s" % (self.sent_at, self.request_type, self.request_origin, self.request_path, self.response_code)
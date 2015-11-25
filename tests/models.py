from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __unicode__(self):
        return "%s" % self.title
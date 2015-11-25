from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns(
    '',
    url(r'^/?$', views.bibs_all, name='index'),
    url(r'^/(?P<bib_id>\d+)/$', views.bibs_detail, name='detail'),
)

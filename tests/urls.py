from django.conf import settings
from django.conf.urls import url, patterns, include
from rest_framework import routers
from bib import views
from .views import ArticleViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"%s/articles/?" % settings.API_VERSION, ArticleViewSet)

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^bib/?", include('bib.urls', namespace='bib')),
]
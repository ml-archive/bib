from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Bib


class BibTests(APITestCase):

    def test_get(self):
        response = self.client.get('/bib', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bib_created(self):
        self.assertEqual(Bib.objects.count(), 0)
        self.client.get('/%s/articles/1' % settings.API_VERSION, format='json')
        self.assertEqual(Bib.objects.count(), 1)
        self.assertEqual(Bib.objects.first().request_type, 'GET')
        self.assertEqual(Bib.objects.first().response_code, '200')

    def test_bib_not_created(self):
        self.assertEqual(Bib.objects.count(), 0)
        self.client.get('/bib', format='json')
        self.assertEqual(Bib.objects.count(), 0)
from django.shortcuts import render_to_response
from .models import Bib

def bibs_all(request):
    bibs = Bib.objects.all().order_by('-sent_at')[:50]
    return render_to_response('bib/all.html', {'bibs': bibs})

def bibs_detail(request, bib_id):
    bib = Bib.objects.get(pk=bib_id)
    return render_to_response('bib/detail.html', {'bib': bib})
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Publication

# Create your views here.
def index(request):
    pubs = Publication.objects.order_by('-pub_date')
    context = { 'publications': pubs }
    return render(request, 'cites/index.html', context)

def pub_detail(request, pub_id):
    pub = get_object_or_404(Publication, pk=pub_id)
    # citations = pub.j
    context = { 'title': pub.title, 'citations': pub.citations.all() }
    return render(request, 'cites/pub_detail.html', context)

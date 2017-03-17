from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from .models import Publication

# Create your views here.
# def index(request):
#     pubs = Publication.objects.order_by('-pub_date')
#     context = { 'publications': pubs }
#     return render(request, 'cites/index.html', context)

######################################
class IndexView(generic.ListView):
    """The list of publications."""
    template_name = 'cites/index.html'
    context_object_name = 'publications'

    def get_queryset(self):
        """Return all publications."""
        return Publication.objects.order_by('-pub_date')

# ######################################
# class PubDetailView(generic.DetailView):
#     """Details of a publication including citations."""
#     model = Publication
#     template_name = 'cites/pub_detail.html'
#
#     def get_queryset(self):
#         """Return all citations for the publication."""
#         return Publication.objects.order_by('-pub_date')

######################################
def pub_detail(request, pk):
    pub = get_object_or_404(Publication, pk=pk)
    # citations = pub.j
    context = { 'publication': pub, 'citations': pub.citations.all() }
    return render(request, 'cites/pub_detail.html', context)

######################################
def add_pub(request):
    """Adds a new publication."""
    title = request.POST["pub_title"]
    title = title.strip()
    if not title:
        return render(request, IndexView.template_name, {
            'error_message': "The title is empty.",
            # the following is horrible solution (copies functionality)
            'publications': Publication.objects.order_by('-pub_date'),
        })

    my_pub = request.POST["pub_my"]
    if my_pub == "on":
        my_pub = True
    else:
        my_pub = False

    newPub = Publication()
    newPub.title = title
    newPub.save()

    return redirect(reverse('cites:index'))






# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

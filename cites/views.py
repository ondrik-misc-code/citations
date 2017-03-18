import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from .models import Publication, Citing, Citation

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

######################################
class ManageView(generic.ListView):
    """Management of publications."""
    template_name = 'cites/manage_pubs.html'
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
    context = {
        'publication': pub,
        'citations': pub.citations.all(),
        'publications': Publication.objects.order_by('-pub_date')
    }

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

######################################
def add_cit(request, pk):
    """Adds a new citation."""
    title = request.POST["cit_title"]
    title = title.strip()
    pub = get_object_or_404(Publication, pk=pk)
    if not title:
        # the following is horrible solution (copies functionality)
        return render(request, 'cites/pub_detail.html', {
            'error_message': "The title is empty.",
            'publication': pub,
            'citations': pub.citations.all(),
            'publications': Publication.objects.order_by('-pub_date')
        })

    str_year = request.POST["cit_year"]
    str_year = str_year.strip()
    error = False
    try:
        year = int(str_year)
        if year < 2000 or year > 2100:
            error = True
    except:
        error = True

    if error:
        # the following is horrible solution (copies functionality)
        return render(request, 'cites/pub_detail.html', {
            'error_message': "The year is invalid.",
            'publication': pub,
            'citations': pub.citations.all(),
            'publications': Publication.objects.order_by('-pub_date')
        })

    newCit = Citing()
    newCit.title = title
    newCit.cited_date = datetime.date(year, 6, 6)
    newCit.save()

    all_pubs = [ pub ]
    other_pubs = request.POST.getlist('also-pubs-checks[]')
    for x in other_pubs:
        tmp_pub = get_object_or_404(Publication, pk=x)
        all_pubs.append(tmp_pub)
        # return HttpResponse("LaLa" + tmp_pub.__str__())

    # return HttpResponse("Ahoj" + all_pubs.__str__())

    # add all bindings
    for x in all_pubs:
        binding = Citation(publication=x, citing=newCit)
        binding.save()

    return redirect(reverse('cites:pub_detail', args=({pk})))


def cit_list_year(request):
    citations = Citation.objects.all()

    cit_map = { }
    for cit in citations:
        year = cit.citing.cited_date.year
        if not year in cit_map:
            cit_map[year] = { }

        if not cit.publication in cit_map[year]:
            cit_map[year][cit.publication] = []

        cit_map[year][cit.publication].append(cit.citing)

    context = {
        'cit_map': cit_map,
    }

    return render(request, 'cites/cit_list_year.html', context)


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

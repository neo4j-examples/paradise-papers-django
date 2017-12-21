from django.shortcuts import render
from django.http import Http404
from .models import *

# Create your views here.
def index(request):
    countries = get_all_countries()
    return render(request , 'search/index.html', {'countries': countries[0] });

def lookup(request):
    node_type = request.GET.get('node')
    country_selected = request.GET.get('country-selected')
    entity_name =  request.GET.get('wordsearch')
    countries = get_all_countries()

    #entities that cointains that name
    entity_nodes = Entity.nodes.filter(name__icontains=entity_name)

    #officers that contains that name
    officer_nodes = Officer.nodes.filter(name__icontains=entity_name)

    #Intermediary that contains that name
    intermediary_nodes = Intermediary.nodes.filter(name__icontains=entity_name)

    if (country_selected != 'allcountry'):
        entity_nodes = entity_nodes.filter(countries__icontains=country_selected)
        officer_nodes = officer_nodes.filter(countries__icontains=country_selected)
        intermediary_nodes = Intermediary.nodes.filter(jurisdiction_description__icontains=country_selected)

    context = {
        'countries': countries[0],
        'word_searched': entity_name,
        'entities': entity_nodes,
        'officers': officer_nodes,
        'intermediaries' : intermediary_nodes,
        'country_selected': country_selected,
        'node_type': node_type

    }

    return render(request , 'search/lookup.html', context );

def nodes(request, node_id):
    try:
        node_info = Entity.nodes.get(node_id=node_id)
        intermediaries = node_info.Intermediary_of()
        officers = node_info.Officer_of()
        context = {
            'node_info': node_info,
            'intermediaries': intermediaries,
            'officers' : officers,
        }
    except Entity.DoesNotExist:
        node_info = Officer.nodes.get(node_id=node_id)
        context = {
            'node_info': node_info,
        }
    return render(request , 'search/nodeSearch.html', context);
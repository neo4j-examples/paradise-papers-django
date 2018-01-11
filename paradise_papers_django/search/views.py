from django.shortcuts import render
from django.http import Http404
from .models import Entity, Officer, Intermediary, get_all_countries, calculatePages
from django.views.generic import TemplateView
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

# Create your views here.
items_Per_Page = 15
class Index(TemplateView):
    template_name = 'search/index.html'

    def get_context_data(self, *args, **kwargs):
        context   = super(Index, self).get_context_data(*args, **kwargs)
        countries = get_all_countries()
        context   = {
            'countries': countries[0]
        }

        return context

class ResultPage(TemplateView):
    template_name = 'search/lookup.html'

    def get_context_data(self, *args, **kwargs):
        context     = super(ResultPage, self).get_context_data(*args, **kwargs)
        node_type   = self.request.GET.get('node')
        country     = self.request.GET.get('country-selected')
        entity_name = self.request.GET.get('wordsearch')
        page = self.request.GET.get('page' , 1 )
        countries   = get_all_countries()
        country_selected = (country, '')[country == 'allcountry']

        #Filtering all nodes
        entity_nodes = Entity.nodes.filter(name__icontains=entity_name).filter(countries__icontains=country_selected)
        officer_nodes = Officer.nodes.filter(name__icontains=entity_name).filter(countries__icontains=country_selected)
        intermediary_nodes = Intermediary.nodes.filter(name__icontains=entity_name).filter(countries__icontains=country_selected)
        
        #counting Nodes
        e_count = len(entity_nodes)
        o_count = len(officer_nodes)
        i_count = len(intermediary_nodes)

        if node_type == 'entity': 
            entity_nodes.limit = items_Per_Page
            entity_nodes.skip = ((int(page) - 1)  * items_Per_Page)
            en_nodes = entity_nodes.all() 
            node_list = range(0,e_count)
            off_nodes=0
            int_nodes=0   

        if node_type == 'officer': 
            officer_nodes.limit = items_Per_Page
            officer_nodes.skip = ((int(page) - 1)  * items_Per_Page)
            off_nodes = officer_nodes.all() 
            node_list = range(0,e_count)
            en_nodes=0
            int_nodes=0

        if node_type == 'intermediary': 
            intermediary_nodes.limit = items_Per_Page
            intermediary_nodes.skip = ((int(page) - 1)  * items_Per_Page)
            int_nodes = intermediary_nodes.all() 
            node_list = range(0,e_count)
            en_nodes=0
            off_nodes=0


        paginator = Paginator(node_list, items_Per_Page)      
        contacts = paginator.page(page)
        page_range = calculatePages(contacts, paginator)
  
        context = {
            'contacts' : contacts,
            'e_count' : e_count,
            'o_count' : o_count,
            'i_count' : i_count,
            'countries': countries[0],
            'word_searched': entity_name,
            'entities': en_nodes,
            'officers': off_nodes,
            'intermediaries' : int_nodes,
            'country_selected': country,
            'node_type': node_type,
            'page_range' : page_range
        }

        return context

def nodes(request, node_id):
    try:
        node_info = Entity.nodes.get(node_id=node_id)
        intermediaries = node_info.intermediaries.all()
        officers = node_info.officers.all()
        addresses = node_info.addressess.all()
        others = node_info.others.all()
        entity = node_info.Entities_relationship();
        context = {
            'node_info': node_info,
            'intermediaries': intermediaries,
            'officers': officers,
            'addresses': addresses,
            'node_type': 'entity',
            'others': others,
            'entity_connections': entity,
        }
    except Entity.DoesNotExist:
            pass
    try:
        node_info = Officer.nodes.get(node_id=node_id)
        entities = node_info.entities.all()
        addresses = node_info.addresses.all()
        context = {
            'node_info': node_info,
            'entities': entities,
            'addresses': addresses,
            'node_type': 'officer',
        }
    except Officer.DoesNotExist:
            pass

    try:
        node_info = Intermediary.nodes.get(node_id=node_id)
        context = {
            'node_info': node_info,
            'node_type': 'intermediary',
        }
    except Intermediary.DoesNotExist:
        pass

    return render(request , 'search/nodeSearch.html', context);

from django.shortcuts import render
from django.http import Http404
from .models import Entity, Officer, Intermediary, helpers
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = 'search/index.html'

    def get_context_data(self, *args, **kwargs):
        context   = super(Index, self).get_context_data(*args, **kwargs)
        countries = helpers.get_all_countries()
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
        countries   = helpers.get_all_countries()

        context = {
            'countries': countries[0],
            'word_searched': entity_name,
            'entities': helpers.filter_by_name_and_contry("entity", entity_name, country),
            'officers': helpers.filter_by_name_and_contry('officer', entity_name, country),
            'intermediaries': helpers.filter_by_name_and_contry('intermediary', entity_name, country),
            'country_selected': country,
            'node_type': node_type
        }

        return context

class NodeDetail(TemplateView):
    template_name = 'search/nodeSearch.html'

    def get_context_data(self, *args, **kwargs):
        context     = super(NodeDetail, self).get_context_data(*args, **kwargs)
        entity_type = self.kwargs.get("slug")
        node_id     = self.kwargs.get("node_id")
        context     = helpers.node_detail(entity_type, node_id)

        return context

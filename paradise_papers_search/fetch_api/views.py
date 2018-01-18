from rest_framework.views import APIView
from rest_framework.response import Response
from .models.helpers import (
    count_nodes,
    fetch_nodes,
    fetch_node_details,
    fetch_countries,
    fetch_jurisdictions
)

class GetNodesCount(APIView):
    def get(self, request):
        count_info = {
            'node_type': request.GET.get('t', 'Entity'),
            'name': request.GET.get('q', ''),
            'country': request.GET.get('c', ''),
            'jurisdiction': request.GET.get('j', ''),
        }
        count = count_nodes(count_info)
        data = {
            'response': {
                'status': '200',
                'data': count,
            },
        }
        return Response(data)

class GetNodesData(APIView):
    def get(self, request):
        fetch_info = {
            'node_type': request.GET.get('t', 'Entity'),
            'name': request.GET.get('q', ''),
            'country': request.GET.get('c', ''),
            'jurisdiction': request.GET.get('j', ''),
            'limit': 10,
            'skip': int(request.GET.get('p', 1)),
        }
        nodes = fetch_nodes(fetch_info)
        data = {
            'response': {
                'status': '200',
                'rows': len(nodes),
                'data': nodes,
            },
        }
        return Response(data)

class GetNodeData(APIView):
    def get(self, request):
        node_info = {
            'node_type': request.GET.get('t', 'Entity'),
            'node_id': int(request.GET.get('id')),
        }
        node_details = fetch_node_details(node_info)
        data = {
            'response': {
                'status': '200',
                'data': node_details,
            },
        }
        return Response(data)

class GetCountries(APIView):
    def get(self, request):
        countries = fetch_countries()
        data = {
            'response': {
                'status': '200',
                'data': countries,
            },
        }
        return Response(data)

class GetJurisdictions(APIView):
    def get(self, request):
        jurisdictions = fetch_jurisdictions()
        data = {
            'response': {
                'status': '200',
                'data': jurisdictions,
            },
        }
        return Response(data)

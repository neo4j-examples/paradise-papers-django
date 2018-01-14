from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models.helpers import count_nodes, fetch_nodes, fetch_node_details

class GetNodesCount(APIView):
    def get(self, request):
        count_info = {
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
        json_data = JSONRenderer().render(data)
        return Response(json_data)

class GetNodesData(APIView):
    def get(self, request):
        fetch_info = {
            'node_type': request.GET.get('t', 'entity'),
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
        json_data = JSONRenderer().render(data)
        return Response(json_data)

class GetNodeData(APIView):
    def get(self, request):
        node_info = {
            'node_type': request.GET.get('t', 'entity'),
            'node_id': int(request.GET.get('id')),
        }
        node_details = fetch_node_details(node_info)
        data = {
            'response': {
                'status': '200',
                'data': node_details,
            },
        }
        json_data = JSONRenderer().render(data)
        return Response(json_data)

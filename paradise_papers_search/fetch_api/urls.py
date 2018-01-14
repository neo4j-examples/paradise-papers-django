from django.conf.urls import url
from .views import (
    GetNodesCount,
    GetNodesData,
    GetNodeData,
)

urlpatterns = [
    url(r'^count[/]?$', GetNodesCount.as_view(), name='get_nodes_count'),
    url(r'^nodes[/]?$', GetNodesData.as_view(), name='get_nodes_data'),
    url(r'^node[/]?$', GetNodeData.as_view(), name='get_node_data'),
]

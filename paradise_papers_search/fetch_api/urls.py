from django.conf.urls import url

from .views import (
    GetNodesCount,
    GetNodesData,
    GetNodeData,
    GetCountries,
    GetJurisdictions,
    GetDataSource,
)


urlpatterns = [
    url(r'^count[/]?$', GetNodesCount.as_view(), name='get_nodes_count'),
    url(r'^nodes[/]?$', GetNodesData.as_view(), name='get_nodes_data'),
    url(r'^node[/]?$', GetNodeData.as_view(), name='get_node_data'),
    url(r'^countries[/]?$', GetCountries.as_view(), name='get_countries'),
    url(r'^jurisdictions[/]?$', GetJurisdictions.as_view(), name='get_jurisdictions'),
    url(r'^datasource[/]?$', GetDataSource.as_view(), name='get_data_source'),
]

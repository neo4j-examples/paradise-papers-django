from django.urls import path

from .views import (
    GetNodesCount,
    GetNodesData,
    GetNodeData,
    GetCountries,
    GetJurisdictions,
    GetDataSource,
)


urlpatterns = [
    path("count/", GetNodesCount.as_view(), name="get_nodes_count"),
    path("nodes/", GetNodesData.as_view(), name="get_nodes_data"),
    path("node/", GetNodeData.as_view(), name="get_node_data"),
    path("countries/", GetCountries.as_view(), name="get_countries"),
    path("jurisdictions/", GetJurisdictions.as_view(), name="get_jurisdictions"),
    path("datasource/", GetDataSource.as_view(), name="get_data_source"),
]

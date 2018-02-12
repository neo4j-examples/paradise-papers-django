from .constants import COUNTRIES, JURISDICTIONS, DATASOURCE

from .models import (
    Entity,
    Address,
    Intermediary,
    Officer,
    Other
)

# For easily access each of the model classes programmatically, create a key-value map.
MODEL_ENTITIES = {
    'Entity': Entity,
    'Address': Address,
    'Intermediary': Intermediary,
    'Officer': Officer,
    'Other': Other
}


###################################################################
# Queries Functions
###################################################################

def filter_nodes(node_type, search_text, country, jurisdiction, source_id):
    node_set = node_type.nodes

    # On Address nodes we want to check the search_text against the address property
    # For any other we check against the name property
    if node_type.__name__ == 'Address':
        node_set.filter(address__icontains=search_text)
    else:
        node_set.filter(name__icontains=search_text)

    # Only entities store jurisdiction info
    if node_type.__name__ == 'Entity':
        node_set.filter(jurisdiction__icontains=jurisdiction)

    node_set.filter(countries__icontains=country)
    node_set.filter(sourceID__icontains=source_id)

    return node_set


def count_nodes(count_info):
    count = {}
    node_type               = count_info['node_type']
    search_word             = count_info['name']
    country                 = count_info['country']
    jurisdiction            = count_info['jurisdiction']
    data_source             = count_info['sourceID']
    node_set                = filter_nodes(MODEL_ENTITIES[node_type], search_word, country, jurisdiction, data_source)
    count['count']          = len(node_set)

    return count


def fetch_nodes(fetch_info):
    node_type       = fetch_info['node_type']
    search_word     = fetch_info['name']
    country         = fetch_info['country']
    limit           = fetch_info['limit']
    start           = ((fetch_info['page'] - 1) * limit)
    end             = start + limit
    jurisdiction    = fetch_info['jurisdiction']
    data_source     = fetch_info['sourceID']
    node_set        = filter_nodes(MODEL_ENTITIES[node_type], search_word, country, jurisdiction, data_source)
    fetched_nodes   = node_set[start:end]

    return [node.serialize for node in fetched_nodes]


def fetch_node_details(node_info):
    node_type       = node_info['node_type']
    node_id         = node_info['node_id']
    node            = MODEL_ENTITIES[node_type].nodes.get(node_id=node_id)
    node_details    = node.serialize

    # Make sure to return an empty array if not connections
    node_details['node_connections'] = []
    if (hasattr(node, 'serialize_connections')):
        node_details['node_connections'] = node.serialize_connections

    return node_details


def fetch_countries():
    return COUNTRIES


def fetch_jurisdictions():
    return JURISDICTIONS


def fetch_data_source():
    return DATASOURCE

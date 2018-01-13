from neomodel import db
from . import (
    Entity,
    Address,
    Intermediary,
    Officer,
    Other
)

MODEL_ENTITIES = {
    'entity': Entity.Entity,
    'address': Address.Address,
    'intermediary': Intermediary.Intermediary,
    'officer': Officer.Officer,
    'other': Other.Other
}

ONLY = [
    'sourceID',
    'address',
    'jurisdiction',
    'service_provider',
    'countries',
    'jurisdiction_description',
    'valid_until',
    'ibcRUC',
    'name',
    'country_codes',
    'incorporation_date',
    'node_id',
    'status',
]

# Serialize data to be JSON parsable
### TODO: Refactor and impplement serializers on models
def serialize_data(obj, main_class, only=None):
    if hasattr(obj, 'definition'):
        obj.definition['node_class'] = None
    if isinstance(obj, (list)):
        for index, item in enumerate(obj):
            if not isinstance(item, (str, int, list, dict)):
                item = serialize_data(item, main_class, only)
            obj[index] = item
        return obj
    if isinstance(obj, dict):
        for key in list(obj):
            if only and key not in only:
                obj.pop(key)
            elif not isinstance(obj[key], (str, int, tuple, list, dict)):
                if type(obj[key]) == MODEL_ENTITIES[main_class]:
                    obj[key] = MODEL_ENTITIES[main_class].__name__
                else:
                    obj[key] = serialize_data(obj[key], main_class)
            elif isinstance(obj[key], (list)):
                obj[key] = list(obj[key])
                for list_index, list_item in enumerate(obj[key]):
                    if not isinstance(list_item, (str, int, list, dict)) and hasattr(list_item, '__dict__'):
                        obj[key][list_index] = serialize_data(list_item.__dict__, main_class, only)

        return obj
    if not isinstance(obj, (str, int, tuple, list, dict)) and hasattr(obj, '__dict__'):

        return serialize_data(obj.__dict__, main_class, only)

    return MODEL_ENTITIES[main_class].__name__

# Count data available for all nodes with a given set of parametters
def count_all_nodes(count_info):
    count = {}
    for node_type in list(MODEL_ENTITIES):
        count_info = dict(count_info)
        count_info['node_type'] = node_type
        count[node_type] = count_nodes(count_info)

    return count

# Queries Functions
def filter_nodes(node_type, name, country, jurisdiction):
    if node_type.__name__ == 'Address':
        node = node_type.nodes.filter(address__icontains=name)
    else:
        node = node_type.nodes.filter(name__icontains=name)
    if node_type.__name__ == 'Other':

        return node
    if jurisdiction:

        return node.filter(jurisdictions__icontains=country)

    return node.filter(countries__icontains=country)

def count_nodes(count_info):
    node_type           = count_info['node_type']
    search_word         = count_info['name']
    country             = count_info['country']
    is_jurisdiction     = count_info['jurisdiction']
    node                = filter_nodes(MODEL_ENTITIES[node_type], search_word, country, is_jurisdiction)
    count_node          = len(node)

    return count_node

def fetch_nodes(fetch_info):
    node_type       = fetch_info['node_type']
    search_word     = fetch_info['name']
    country         = fetch_info['country']
    limit           = fetch_info['limit']
    skip            = ((fetch_info['skip'] - 1) * limit)
    is_jurisdiction = fetch_info['jurisdiction']
    node            = filter_nodes(MODEL_ENTITIES[node_type], search_word, country, is_jurisdiction)
    node.limit      = limit
    node.skip       = skip
    fetched_nodes   = node.all()

    return serialize_data(fetched_nodes, node_type, ONLY)

def entities_relationship(self):
    results = self.cypher("START p=node({self}) MATCH n=(p)<-[r]->(x:Entity) RETURN r, x.node_id as Node_id")
    list    = []

    for row in results[0]:
        list.append((row[0].type, self.nodes.get(node_id=row[1])))

    return list

def fetch_node_details(node_info):
    node_type = node_info['node_type']
    node_id = node_info['node_id']
    node = MODEL_ENTITIES[node_type].nodes.get(node_id=node_id)

    if (node_type == 'entity'):
        intermediaries = node.intermediaries.all()
        officers       = node.officers.all()
        addresses      = node.addressess.all()
        others         = node.others.all()
        entity         = entities_relationship(node)

        return  {
            'node_info': serialize_data(node, node_type),
            'intermediaries': serialize_data(intermediaries, node_type),
            'officers': serialize_data(officers, node_type),
            'addresses': serialize_data(addresses, node_type),
            'others': serialize_data(others, node_type),
            'entity_connections': serialize_data(entity, node_type),
        }
    elif (node_type == 'officer'):
        entities  = node.entities.all()
        addresses = node.addresses.all()

        return {
            'node_info': serialize_data(node, node_type),
            'entities': serialize_data(entities, node_type),
            'addresses': serialize_data(addresses, node_type),
        }
    else:

        return {
            'node_info': serialize_data(node, node_type),
        }

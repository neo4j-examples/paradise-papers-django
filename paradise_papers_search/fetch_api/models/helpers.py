from neomodel import db, RelationshipManager
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

# Queries Functions
def filter_nodes(entity, name, country, jurisdiction):
    if jurisdiction:
        return entity.nodes.filter(name__icontains=name).filter(jurisdictions__icontains=country)

    return entity.nodes.filter(name__icontains=name).filter(countries__icontains=country)

def count_nodes(count_info):
    entity      = count_info['entity']
    search_word = count_info['name']
    country     = count_info['country']
    is_jurisdiction = count_info['jurisdiction']
    node = filter_by_name_and_contry(MODEL_ENTITIES[entity], search_word, country, is_jurisdiction)
    count_node  = len(node)

    return count_node

def fetch_nodes(fetch_info):
    entity          = fetch_info['entity']
    search_word     = fetch_info['name']
    country         = fetch_info['country']
    limit           = fetch_info['limit']
    skip            = ((fetch_info['skip'] - 1) * limit)
    is_jurisdiction = count_info['jurisdiction']
    node            = filter_by_name_and_contry(MODEL_ENTITIES[entity], search_word, country, is_jurisdiction)
    node.limit      = limit
    node.skip       = skip
    fetch_node      = node.all()

    return fetch_node

def entities_relationship(self):
    results = self.cypher("START p=node({self}) MATCH n=(p)<-[r]->(x:Entity) RETURN r, x.node_id as Node_id")
    list    = []

    for row in results[0]:
        list.append((row[0].type, self.nodes.get(node_id=row[1])))

    return list

def node_detail(node_info):
    entity_type = node_info['entity']
    node_id = node_info['node_id']
    node = MODEL_ENTITIES[entity_type].nodes.get(node_id=node_id)

    if (entity_type == 'entity'):
        intermediaries = node.intermediaries.all()
        officers       = node.officers.all()
        addresses      = node.addressess.all()
        others         = node.others.all()
        entity         = entities_relationship(node)

        return  {
            'node_info': node,
            'intermediaries': intermediaries,
            'officers': officers,
            'addresses': addresses,
            'others': others,
            'entity_connections': entity,
        }
    elif (entity_type == 'officer'):
        entities  = node.entities.all()
        addresses = node.addresses.all()
        return {
            'node_info': node,
            'entities': entities,
            'addresses': addresses
        }
    else:
        return {
            'node_info': node
        }

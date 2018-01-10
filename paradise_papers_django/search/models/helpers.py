from neomodel import db
from . import (
    Entity,
    Address,
    Intermediary,
    Officer,
    Other
)

MODELENTITIES = {
'entity': Entity.Entity,
'address': Address.Address,
'intermediary': Intermediary.Intermediary,
'officer': Officer.Officer,
'other': Other.Other
}

# Queries Functions
def get_all_countries():
    query = "MATCH (n) WHERE NOT n.countries CONTAINS ';' RETURN DISTINCT 'node' as entity, n.countries AS countries UNION ALL MATCH ()-[r]-() WHERE EXISTS(r.countries) RETURN DISTINCT 'relationship' AS entity, r.countries AS countries"
    results = db.cypher_query(query)
    return results

def filter_by_name_and_contry(entity, name, country):
    country_selected = (country, '')[country == 'allcountry']
    entity_node = MODELENTITIES[entity].nodes.filter(name__icontains=name).filter(countries__icontains=country_selected)

    return entity_node

def entities_relationship(self):
    results = self.cypher("START p=node({self}) MATCH n=(p)<-[r]->(x:Entity) RETURN r, x.node_id as Node_id")
    list = []

    for row in results[0]:
        list.append((row[0].type, self.nodes.get(node_id=row[1])))

    return list

def node_detail(entity_type, node_id):
    node_info = MODELENTITIES[entity_type].nodes.get(node_id=node_id)

    if (entity_type == 'entity'):
        intermediaries = node_info.intermediaries.all()
        officers       = node_info.officers.all()
        addresses      = node_info.addressess.all()
        others         = node_info.others.all()
        entity         = entities_relationship(node_info);

        context = {
            'node_info': node_info,
            'intermediaries': intermediaries,
            'officers': officers,
            'addresses': addresses,
            'node_type': entity_type,
            'others': others,
            'entity_connections': entity,
        }
    elif (entity_type == 'officer'):
        entities = node_info.entities.all()
        addresses = node_info.addresses.all()
        context = {
            'node_info': node_info,
            'entities': entities,
            'addresses': addresses,
            'node_type': entity_type,
        }
    else:
        context = {
            'node_info': node_info,
            'node_type': entity_type,
        }

    return context

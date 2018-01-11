from django.db import models
from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Class for Neo4j databaser nodes
class Entity(DjangoNode):
    sourceID = StringProperty()
    jurisdiction = StringProperty()
    service_provider = StringProperty()
    countries = StringProperty()
    jurisdiction_description =  StringProperty()
    valid_until = StringProperty()
    name = StringProperty()
    incorporation_date=StringProperty()
    node_id = StringProperty()
    status = StringProperty()
    officers = RelationshipFrom('Officer', 'OFFICER_OF')
    intermediaries = RelationshipFrom('Intermediary', 'INTERMEDIARY_OF')
    addressess = RelationshipTo('Address', 'REGISTERED_ADDRESS')
    others = RelationshipFrom('Other', 'CONNECTED_TO')
    def Entities_relationship(self):
        results = self.cypher("START p=node({self}) MATCH n=(p)<-[r]->(x:Entity) RETURN r, x.node_id as Node_id");
        list =[];
        for row in results[0]:
            list.append((row[0].type, Entity.nodes.get(node_id=row[1])))
        return list


class Other(DjangoNode):
    sourceID = StringProperty()
    name = StringProperty()
    valid_until = StringProperty()
    node_id = StringProperty()

class Intermediary(DjangoNode):
    sourceID = StringProperty()
    valid_until = StringProperty()
    name = StringProperty()
    country_codes = StringProperty()
    countries = StringProperty()
    node_id = StringProperty()
    status = StringProperty()

class Officer(DjangoNode):
    sourceID = StringProperty()
    name = StringProperty()
    country_codes = StringProperty()
    valid_until = StringProperty()
    countries = StringProperty()
    node_id = StringProperty()
    addresses = RelationshipTo('Address', 'REGISTERED_ADDRESS')
    entities = RelationshipTo('Entity', 'OFFICER_OF')



class Address(DjangoNode):
    sourceID = StringProperty()
    country_codes = StringProperty()
    valid_until = StringProperty()
    address = StringProperty()
    countries = StringProperty()
    node_id = StringProperty()

# Queries Functions
def get_all_countries():
    return db.cypher_query("MATCH (n) WHERE NOT n.countries CONTAINS ';' RETURN DISTINCT  n.countries AS countries")

install_labels(Entity)
install_labels(Other)
install_labels(Intermediary)
install_labels(Officer)
install_labels(Address)

def calculatePages(contacts, paginator):
    max_index = len(paginator.page_range)
    index = contacts.number - 1
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    return list(paginator.page_range)[start_index:end_index]

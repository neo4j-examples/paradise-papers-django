from django.db import models
from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode

#Class for Neo4j databaser nodes
class Entity(DjangoNode):
    sourceID = StringProperty()
    address = StringProperty()
    jurisdiction = StringProperty()
    service_provider = StringProperty()
    countries = StringProperty()
    jurisdiction_description =  StringProperty()
    valid_until = StringProperty()
    ibcRUC = StringProperty()
    name = StringProperty()
    country_codes = StringProperty()
    incorporation_date=StringProperty()
    node_id = StringProperty()
    status = StringProperty()
    officers = RelationshipFrom('Officer', 'OFFICER_OF')
    intermediaries = RelationshipFrom('Intermediary', 'INTERMEDIARY_OF')
    addresses = RelationshipTo('Address', 'REGISTERED_ADDRESS')
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
    intermediaries = RelationshipTo('Intermediary', 'OFFICER_OF')
    others = RelationshipTo('Other', 'OFFICER_OF')

    def officers_relationship(self):
        results = self.cypher("START p=node({self}) MATCH n=(p)<-[r]->(x:Officer) RETURN r, x.node_id as Node_id");
        list =[];
        for row in results[0]:
            list.append((row[0].type, Officer.nodes.get(node_id=row[1])))
        return list



class Address(DjangoNode):
    sourceID = StringProperty()
    country_codes = StringProperty()
    valid_until = StringProperty()
    address = StringProperty()
    countries = StringProperty()
    node_id = StringProperty()

# Queries Functions
def get_all_countries():
    query = "MATCH (n) WHERE NOT n.countries CONTAINS ';' RETURN DISTINCT 'node' as entity, n.countries AS countries UNION ALL MATCH ()-[r]-() WHERE EXISTS(r.countries) RETURN DISTINCT 'relationship' AS entity, r.countries AS countries"
    results = db.cypher_query(query)
    return results

install_labels(Entity)
install_labels(Other)
install_labels(Intermediary)
install_labels(Officer)
install_labels(Address)

from django.db import models
from neomodel import *
from neomodel import db
from django_neomodel import DjangoNode

# config.DATABASE_URL = 'bolt://paradisepapers:paradisepapers@165.227.223.190:7687'
# Create your models here.


#Class for Neo4j databaser nodes
class Entity(DjangoNode):
    sourceID = StringProperty()
    address = StringProperty()
    jurisdiction = StringProperty()
    service_provider = StringProperty()
    countries = StringProperty()
    jurisdiction_description =  StringProperty()
    valid_unti = StringProperty()
    ibcRUC = StringProperty()
    name = StringProperty()
    country_codes = StringProperty()
    incorporation_date=StringProperty()
    node_id = StringProperty()
    status = StringProperty()

    def Intermediary_of(self):
        results = self.cypher("START p=node({self}) MATCH n=(x)-[r:INTERMEDIARY_OF]->(p) RETURN x LIMIT 25")
        return [self.inflate(row[0]) for row in results[0]]

    def Officer_of(self):
        results =  self.cypher("START p=node({self}) MATCH n=(x)-[r:OFFICER_OF]->(p) RETURN x LIMIT 25")
        return [self.inflate(row[0]) for row in results[0]]
class Other(DjangoNode):
    sourceID = StringProperty()
    name = StringProperty()
    valid_unti = StringProperty()
    node_id = IntegerProperty()

class Intermediary(DjangoNode):
    name = StringProperty()
    pagerank_g = StringProperty()
    jurisdiction_description = StringProperty()
    jurisdiction = StringProperty()
    node_id = StringProperty()

class Officer(DjangoNode):
    sourceID = StringProperty()
    name = StringProperty()
    country_codes = StringProperty()
    valid_unti = StringProperty()
    countries = StringProperty()
    node_id = StringProperty()

class Adress(DjangoNode):
    sourceID = StringProperty()
    country_codes = StringProperty()
    valid_unti = StringProperty()
    address = StringProperty()
    countries = StringProperty()
    node_id = IntegerProperty()

# Queries Functions
def get_all_countries():
    query = "MATCH (n) WHERE NOT n.countries CONTAINS ';' RETURN DISTINCT 'node' as entity, n.countries AS countries UNION ALL MATCH ()-[r]-() WHERE EXISTS(r.countries) RETURN DISTINCT 'relationship' AS entity, r.countries AS countries"
    results =  db.cypher_query(query)
    return results


install_labels(Entity)
install_labels(Other)
install_labels(Intermediary)
install_labels(Officer)
install_labels(Adress)

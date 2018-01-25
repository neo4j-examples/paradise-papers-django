from abc import ABCMeta
from neomodel import db


class NodeUtils:
    __metaclass__ = ABCMeta

    @classmethod
    def serialize_relationships(cls, nodes, relationship):
        serialized_nodes = []
        for node in nodes:
            serialized_node = node.serialize
            serialized_node['node_relationship'] = relationship
            serialized_nodes.append(serialized_node)

        return serialized_nodes

    def serialized_realtionships_of_type(self, node_type):
        results = self.cypher('''
            START p=node({self})
            MATCH n=(p)<-[r]->(x:%s)
            RETURN r, x.node_id as Node_id
            '''%(node_type)
        )
        nodes   = []

        for row in results[0]:
            node = db.cypher_query(
                '''
                MATCH (n:%s) WHERE id(n) = %s RETURN n
                '''
            )%(node_type, row[1])
            serialized_node = node.serialize
            serialized_node['node_relationship'] = row[0].type
            nodes.append(serialized_node)

        return nodes

from neomodel import db

countries = db.cypher_query(
    '''
    MATCH (n)
    WHERE NOT n.countries CONTAINS ';'
    RETURN DISTINCT n.countries AS countries
    '''
)[0]

jurisdictions = db.cypher_query(
    '''
    MATCH (n)
    RETURN DISTINCT n.jurisdiction AS jurisdiction
    '''
)[0]


COUNTRIES = sorted([country[0] for country in countries])
JURISDICTIONS = sorted([jurisdiction[0] for jurisdiction in jurisdictions if isinstance(jurisdiction[0], str)])

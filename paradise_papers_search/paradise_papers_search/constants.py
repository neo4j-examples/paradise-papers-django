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

data_sources = db.cypher_query(
	'''
	MATCH (n)
	RETURN DISTINCT n.sourceID AS dataSource
	'''
)[0]

COUNTRIES = sorted([country[0] for country in countries])
JURISDICTIONS = sorted([jurisdiction[0] for jurisdiction in jurisdictions if isinstance(jurisdiction[0], str)])
DATASOURCE = sorted([data_source[0] for data_source in data_sources if isinstance(data_source[0], str)])

import sys
import csv

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

# Import declared types for New Relic GraphQL schema
# Generated using:
# $ python3 -m sgqlc.introspection --exclude-deprecated --exclude-description \
#   -H "API-Key: <redacted>" \
#   hhttps://api.newrelic.com/graphql \
#   newrelic_schema.json
# $ sgqlc-codegen newrelic_schema.json newrelic_schema.py
from newrelic_schema import newrelic_schema as schema

url = 'https://api.newrelic.com/graphql'
headers = {'API-Key': sys.argv[1]}
endpoint = HTTPEndpoint(url, headers)


def get_application_entities(cluster="prod"):
    """
    Return all guids for the specified cluster.
    """
    op = Operation(schema.RootQueryType)
    results = op.actor.entity_search(query="type IN ('APPLICATION')").results
    results.entities.__fields__('guid', 'name')
    results.next_cursor()
    data = endpoint(op)

    entity_search_results = (op + data).actor.entity_search.results
    entities = entity_search_results.entities
    cursor = entity_search_results.next_cursor

    while cursor is not None:
        op = Operation(schema.RootQueryType)
        results = op.actor.entity_search(query="type IN ('APPLICATION')").\
            results(cursor=cursor)
        results.next_cursor()
        results.entities.__fields__('guid', 'name', 'tags')
        results.entities.tags.__fields__()
        data = endpoint(op)

        entity_search_results = (op + data).actor.entity_search.results

        entities.extend(entity_search_results.entities)
        cursor = entity_search_results.next_cursor

    cluster_entities = []
    for entity in entities:
        try:
            for tag in entity.tags:
                if tag.key.lower() == "cluster":
                    for c in tag.values:
                        if c.lower() == cluster:
                            cluster_entities.append(entity)
        except AttributeError:
            if "(" + cluster.lower() + ")" in entity.name.lower():
                cluster_entities.append(entity)

    return [(entity.guid, entity.name) for entity in cluster_entities]


def build_call_relationships(entities):
    """
    Given a list of guids, return all CALL relationship types
    """
    # Build a lookup table from entity to array index
    entity_lookup = {}
    i = 0
    for entity in entities:
        entity_lookup[entity] = i
        i = i + 1

    # Build a matrix out of CALLS relationships between entities
    # 1 entries mean a call for i to j, 0 means no call
    size = len(entities)
    calls = [[0]*size for i in range(size)]

    for e in entities:
        # Query for relationships
        guid, _ = e
        op = Operation(schema.RootQueryType)
        query = op.actor.entity(guid=guid)
        query.name()
        query.guid()
        query.relationships.source.entity.name()
        query.relationships.source.guid()
        query.relationships.target.entity.name()
        query.relationships.target.guid()
        query.relationships.type()

        data = endpoint(op)

        # Find calls relationships
        j_idx = entity_lookup[e]
        entity = (op + data).actor.entity
        for relationship in entity.relationships:
            if relationship.type == "CALLS":
                rel_entity = (relationship.target.guid,
                              relationship.target.entity.name)

                try:
                    i_idx = entity_lookup[rel_entity]
                    calls[i_idx][j_idx] = 1
                except KeyError:
                    continue

    return calls


def write_to_csv(entities, calls, outfile="out.csv"):
    """
    Write the list of calls to a CSV file matching CAM format.
    """
    with open(outfile, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["ELEMENT NAME", "HIERARCHY ID"] +
                        list(range(1, len(entities)+1)))

        for i in range(len(entities)):
            row = []
            row.append(entities[i][1])
            row.append(i+1)
            for j in range(len(entities)):
                if calls[i][j] == 1:
                    row.append(1)
                else:
                    row.append(" ")

            writer.writerow(row)


outfile = "out.csv"
try:
    outfile = sys.argv[2]
except IndexError:
    pass

entities = get_application_entities("prod")
calls = build_call_relationships(entities)
write_to_csv(entities, calls, outfile)

from pyshacl import validate
from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import rdflib, json, base64, requests

# input
data = rdflib.Graph().parse("entities/BRS_43-500C.ttl", format="ttl")
shape = rdflib.Graph().parse("schema.ttl", format="ttl")

# processing
result = validate(data, shacl_graph=shape, inference='rdfs')
conforms, results_graph, results_text = result
jsonLD = results_graph.serialize(format='json-ld').decode("utf-8")
results_json = json.loads(jsonLD)

# output
print(results_text)
print(results_json)
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, OWL

BASE_URI = f"http://www.di.uminho.pt/rpcw2026/PG61516#"
RPCW = Namespace(BASE_URI)

g = Graph()
g.bind("rpcw", RPCW)
ontologia_uri = URIRef(f"http://www.di.uminho.pt/rpcw2026/PG61516")
g.add((ontologia_uri, RDF.type, OWL.Ontology))

# Classes
classes = ["Jogo", "Autor", "Editora", "Mecanica", "Premio"]
for c in classes:
    g.add((RPCW[c], RDF.type, OWL.Class))

# Object Properties 
object_properties = ["designedGame", "publishedGame", "usedInGame", "wonByGame"]
for op in object_properties:
    g.add((RPCW[op], RDF.type, OWL.ObjectProperty))

# Data Properties 
data_properties = [
    "name", "category", "descriptionEN", "country", 
    "minPlayers", "maxPlayers", "playingTimeMinutes", "year" 
]
for dp in data_properties:
    g.add((RPCW[dp], RDF.type, OWL.DatatypeProperty))

def sanitize_id(string_id):
    return string_id.strip().replace(" ", "_").replace('"', '')

output_file = "boardgames_base.ttl"
g.serialize(destination=output_file, format="turtle")
print(f"Ontologia gerada com sucesso e guardada em '{output_file}'.")
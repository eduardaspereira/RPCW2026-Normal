import json
import os
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, OWL, XSD

# 1. Configuração Inicial e Namespace
BASE_URI = f"http://www.di.uminho.pt/rpcw2026/PG61516#"
RPCW = Namespace(BASE_URI)

g = Graph()
g.bind("rpcw", RPCW)

# Definir a ontologia
ontologia_uri = URIRef(f"http://www.di.uminho.pt/rpcw2026/PG61516")
g.add((ontologia_uri, RDF.type, OWL.Ontology))

# 2. Definir a Estrutura Base (Classes)
classes = ["Jogo", "Autor", "Editora", "Mecanica", "Premio"]
for c in classes:
    g.add((RPCW[c], RDF.type, OWL.Class))

# 3. Data Properties e Object Properties
# Object Properties (Relações entre indivíduos)
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

# 4. Carregar JSONs
def load_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    print(f"Aviso: Ficheiro {filename} não encontrado.")
    return []

def sanitize_id(string_id):
    return string_id.strip().replace(" ", "_").replace('"', '')

# 5. Povoamento da Ontologia

# 5.1 Carregar Jogos
jogos = load_json("jogos.json")
for jogo in jogos:
    j_uri = RPCW[sanitize_id(jogo["id"])]
    g.add((j_uri, RDF.type, RPCW.Jogo))
    
    if "name" in jogo:
        g.add((j_uri, RPCW.name, Literal(jogo["name"], datatype=XSD.string)))
    if "category" in jogo:
        g.add((j_uri, RPCW.category, Literal(jogo["category"], datatype=XSD.string)))
    if "descriptionEN" in jogo:
        g.add((j_uri, RPCW.descriptionEN, Literal(jogo["descriptionEN"], datatype=XSD.string)))
    if "minPlayers" in jogo:
        g.add((j_uri, RPCW.minPlayers, Literal(jogo["minPlayers"], datatype=XSD.integer)))
    if "maxPlayers" in jogo:
        g.add((j_uri, RPCW.maxPlayers, Literal(jogo["maxPlayers"], datatype=XSD.integer)))
    if "playingTimeMinutes" in jogo:
        g.add((j_uri, RPCW.playingTimeMinutes, Literal(jogo["playingTimeMinutes"], datatype=XSD.integer)))

# 5.2 Carregar Autores
autores = load_json("autores.json")
for autor in autores:
    a_uri = RPCW[sanitize_id(autor["id"])]
    g.add((a_uri, RDF.type, RPCW.Autor))
    
    if "name" in autor:
        g.add((a_uri, RPCW.name, Literal(autor["name"], datatype=XSD.string)))
    
    if "designedGames" in autor:
        for jogo_id in autor["designedGames"]:
            g.add((a_uri, RPCW.designedGame, RPCW[sanitize_id(jogo_id)]))

# 5.3 Carregar Editoras
editoras = load_json("editoras.json")
for editora in editoras:
    e_uri = RPCW[sanitize_id(editora["id"])]
    g.add((e_uri, RDF.type, RPCW.Editora))
    
    if "name" in editora:
        g.add((e_uri, RPCW.name, Literal(editora["name"], datatype=XSD.string)))
    if "country" in editora:
        g.add((e_uri, RPCW.country, Literal(editora["country"], datatype=XSD.string)))
    
    if "publishedGames" in editora:
        for jogo_id in editora["publishedGames"]:
            g.add((e_uri, RPCW.publishedGame, RPCW[sanitize_id(jogo_id)]))

# 5.4 Carregar Mecânicas
mecanicas = load_json("mecanicas.json")
for mecanica in mecanicas:
    m_uri = RPCW[sanitize_id(mecanica["id"])]
    g.add((m_uri, RDF.type, RPCW.Mecanica))
    
    if "name" in mecanica:
        g.add((m_uri, RPCW.name, Literal(mecanica["name"], datatype=XSD.string)))
    
    if "usedInGames" in mecanica:
        for jogo_id in mecanica["usedInGames"]:
            g.add((m_uri, RPCW.usedInGame, RPCW[sanitize_id(jogo_id)]))

# 5.5 Carregar Prémios
premios = load_json("premios.json")
for premio in premios:
    p_uri = RPCW[sanitize_id(premio["id"])]
    g.add((p_uri, RDF.type, RPCW.Premio))
    
    if "name" in premio:
        g.add((p_uri, RPCW.name, Literal(premio["name"], datatype=XSD.string)))
    if "year" in premio:
        g.add((p_uri, RPCW.year, Literal(premio["year"], datatype=XSD.integer)))
    
    if "wonByGame" in premio:
        g.add((p_uri, RPCW.wonByGame, RPCW[sanitize_id(premio["wonByGame"])]))

# 6. Gravar o resultado
output_file = "boardgames_ind.ttl"
g.serialize(destination=output_file, format="turtle")
print(f"Ontologia gerada com sucesso e guardada em '{output_file}'.")
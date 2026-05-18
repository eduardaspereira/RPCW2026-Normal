# RPCW Normal

## Metainformação
* **Título:** Teste
* **Data:** 18-05-2026
* **Autor:**
    * **Id:** PG61516
    * **Nome:** Eduarda Pereira

## Resumo
Este repositório contém as respostas aos 2 exercícios do teste. Cada exercício inclui a definição da ontologia base, instanciação de dados e consultas SPARQL para exploração do conhecimento.

## Estrutura do Repositório

### Exercício 1 - Ontologia de uma Fábula

**Ficheiros:**
* [fabula.ttl](ex1/fabula.ttl): Ontologia e instâncias da fábula
* [queries.txt](ex1/queries.txt): Conjunto de 4 consultas SPARQL para explorar os dados

**O que foi feito:**
- Definição de classes: `Personagem`, `Animal` (subclasse de Personagem), `Objeto`, `Sentimento_Caracteristica`
- Definição de object properties: `enganou`, `localizadoEm`, `possuiObjeto`, `temCaracteristica`
- Definição de data properties: `nome` 

---
### Exercício 2 - Ontologia de Jogos de Tabuleiro
Modelagem de um catálogo de jogos de tabuleiro com autores, editoras, mecânicas e prémios.

**Ficheiros:**
* [base.py](ex2/base.py): Script Python que gera a ontologia base
* [povoar_ontologia.py](ex2/povoar_ontologia.py): Script Python que popula a ontologia com dados dos JSONs
* [boardgames_base.ttl](ex2/boardgames_base.ttl): Ontologia base gerada (output de base.py)
* [boardgames_ind.ttl](ex2/boardgames_ind.ttl): Ontologia populada com instâncias (output de povoar_ontologia.py)
* [sparql.txt](ex2/sparql.txt): Consultas SPARQL 
* **Dados (JSONs):** 
  * [autores.json](ex2/autores.json)
  * [editoras.json](ex2/editoras.json)
  * [jogos.json](ex2/jogos.json)
  * [mecanicas.json](ex2/mecanicas.json)
  * [premios.json](ex2/premios.json)

**O que foi feito:**

**Definição da Ontologia Base (base.py):**
- Definição de 5 classes: `Jogo`, `Autor`, `Editora`, `Mecanica`, `Premio`
- Definição de 4 object properties (relações): 
  - `designedGame` (Autor → Jogo)
  - `publishedGame` (Editora → Jogo)
  - `usedInGame` (Mecanica → Jogo)
  - `wonByGame` (Premio → Jogo)
- Definição de 8 data properties:
  - `name`
  - `category`
  - `descriptionEN` 
  - `country` 
  - `minPlayers`
  - `maxPlayers`
  - `playingTimeMinutes` 
  - `year`

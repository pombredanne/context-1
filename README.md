# context
Context is an educational software that models real world into graphs using NLP.

It uses Python's NLTK to process text and Py2Neo to create Neo4j graphs from it. 

**Dependencies**
```
nltk=3.2.2
neo4j=3.1.1
py2neo=3.1.2
```

To install the dependencies, go to Terminal and type the following:
```
$ sudo apt-get install nltk
$ sudo apt-get install neo4j
$ sudo -H python3 -m pip install py2neo
```

After that...
- Fork and clone this repo.
- Configure Neo4j in browser and edit `db.py` 
- Edit the text in `test.py` and run.

**Update**: For now, Context can model the standard SVO (Subject-Verb-Object) format with adjectives. More to come!

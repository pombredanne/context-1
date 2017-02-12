# connects 'py2neo' to 'neo4j'

from py2neo.database.auth import authenticate

# login details (EDIT)
user = "neo4j"
password = "0000"

authenticate("localhost:7474", user, password)

# write to 'graph.db' by default
db = "http://localhost:7474/db/graph"

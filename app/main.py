from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from .graphql.schema import schema
from .database import engine
from .models import Base
from .data_loader.load_data import load_data

app = FastAPI()

# Vytvoření databázových tabulek
Base.metadata.create_all(bind=engine)

# Načtení dat z PDF při inicializaci
load_data('path_to_shadowrun_rules.pdf', list(range(80, 98)))

# Nastavení GraphQL endpointu
app.add_route("/graphql", GraphQLApp(schema=schema))

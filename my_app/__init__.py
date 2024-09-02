from flask import Flask
from flask_graphql import GraphQLView

from .data import setup
from .schema import schema

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    db_path = "./data/test/" if app.testing else "./data/"
    setup(db_path)

    app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))

    return app

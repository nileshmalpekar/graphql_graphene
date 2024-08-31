from database import init_db
from data import setup
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
app.debug = True

default_query = """
query {
        users {
            firstName,
            lastName
        }
    }
""".strip()

app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))

if __name__ == "__main__":
    init_db()
    setup()
    app.run()


import os
from my_app import create_app, create_database

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app('flask.cfg')

def get_mongodb_uri():
    username = os.getenv("MONGODB_USERNAME")
    password = os.getenv("MONGODB_PASSWORD")
    host = os.getenv("MONGODB_HOSTNAME")
    db = os.getenv("MONGODB_DATABASE")
    mongo_uri = f'mongodb://{username}:{password}@{host}/{db}'
    return mongo_uri


create_database(app, get_mongodb_uri())

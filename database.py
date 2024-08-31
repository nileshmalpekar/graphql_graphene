import mongomock
from mongoengine import connect

from models import User

connect('graphene-mongo-example', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)

def init_db():
    nm = User(first_name="Nilesh", last_name="Malpekar")
    nm.save()

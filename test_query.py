from graphene.test import Client
from database import init_db
from data import setup
from schema import schema

init_db()
setup()

client = Client(schema)

def test_users():
    result = client.execute("""query { users { firstName, lastName, fullName }}""")
    assert result == {"data": {"users": [
        {"firstName": "Nilesh", "lastName": "Malpekar", "fullName": "Nilesh Malpekar"}
        ]}}

def test_entities():
    result = client.execute("""query { entities { id, title }}""")
    assert result == {"data": {"entities": [ 
        {"id": "claim", "title": "Claim"}, 
        {"id": "claim_part", "title": "Claim Participant"},
        {"id": "claim_asset", "title": "Claim Asset"}
        ]}}


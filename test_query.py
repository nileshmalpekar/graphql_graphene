from graphene.test import Client
from database import init_db
from schema import schema

init_db()

client = Client(schema)

def test_users_query():
    result = client.execute("""query { users { firstName, lastName, fullName }}""")
    assert result == {"data": {"users": [
        {"firstName": "Nilesh", "lastName": "Malpekar", "fullName": "Nilesh Malpekar"}
        ]}}


from graphene.test import Client
import pytest

from my_app import data
from my_app import schema

data.setup("./data/test/")

grapheneClient = Client(schema)

def test_query_using_files(input, output):
    q,v = input
    result = grapheneClient.execute(q, variables=v)
    assert result == output

def test_http_data(client, payload, output):
    response = client.post("/graphql", json=payload)

    assert 200 == response.status_code
    assert output == response.json

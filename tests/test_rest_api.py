import pytest

def test_index(client):
    payload = {"query": "query { models { id } }", "variables": None}
    response = client.post("/graphql", json=payload)

    assert 200 == response.status_code
    models = response.json["data"]["models"]
    assert 3 == len(models)
    assert [{"id": "m1"},{"id": "m2"},{"id": "m3"}] == models

from graphene.test import Client
# from database import init_db
from data import setup
from schema import schema

# init_db()
setup(path='./data/test/')

client = Client(schema)

# def test_users():
#     result = client.execute("""query { users { firstName, lastName, fullName }}""")
#     assert result == {"data": {"users": [
#         {"firstName": "Nilesh", "lastName": "Malpekar", "fullName": "Nilesh Malpekar"}
#         ]}}

def test_entities():
    result = client.execute("""query { entities { id, title, primaryKey, belongsTo { entityId, foreignKey} }}""")
    assert result == {"data": {"entities": [ 
        {"id": "claim", "title": "Claim", "primaryKey": ["claim_id"], "belongsTo": None}, 
        {"id": "claim_part", "title": "Claim Participant", "primaryKey": ["part_id"], "belongsTo": [{ "entityId": "claim", "foreignKey": ["claim_id"]}]},
        {"id": "claim_asset", "title": "Claim Asset", "primaryKey": ["asset_id"], "belongsTo": [{ "entityId": "claim", "foreignKey": ["claim_id"]}]},
        {"id": "claim_part_injr", "title": "Claim Participant Injury", "primaryKey": ["injr_id"], "belongsTo": [{ "entityId": "claim_part", "foreignKey": ["part_id"]}]}
        ]}}


def test_entities_resolved_entity_parent():
    result = client.execute("""query { entities { id, belongsTo { entity { id } } }}""")
    assert result == {"data": {"entities": [ 
        {"id": "claim", "belongsTo": None}, 
        {"id": "claim_part", "belongsTo": [{ "entity": { "id": "claim"}}]},
        {"id": "claim_asset", "belongsTo": [{ "entity": { "id": "claim"}}]},
        {"id": "claim_part_injr", "belongsTo": [{ "entity": { "id": "claim_part"}}]}
        ]}}


def test_entities_resolved_children_entities():
    result = client.execute("""query { entities { id, childrenEntities { id } }}""")
    assert result == {"data": {"entities": [ 
        {"id": "claim", "childrenEntities": [{"id": "claim_part"}, {"id": "claim_asset"}]}, 
        {"id": "claim_part", "childrenEntities": [{"id": "claim_part_injr"}]},
        {"id": "claim_asset", "childrenEntities": []},
        {"id": "claim_part_injr", "childrenEntities": []}
        ]}}


def test_entities_resolved_parent_entities():
    result = client.execute("""query { entities { id, parentEntities { id } }}""")
    assert result == {"data": {"entities": [ 
        {"id": "claim", "parentEntities": []}, 
        {"id": "claim_part", "parentEntities": [{"id": "claim"}]},
        {"id": "claim_asset", "parentEntities": [{"id": "claim"}]},
        {"id": "claim_part_injr", "parentEntities": [{"id": "claim_part"}]}
        ]}}


def test_entities_resolved_insights():
    result = client.execute("""query { entities { id, insights { id } }}""")
    assert result == {"data": {"entities": [ 
        {"id": "claim", "insights": []}, 
        {"id": "claim_part", "insights": [{"id": "BII"}]},
        {"id": "claim_asset", "insights": [{"id": "TL"}]},
        {"id": "claim_part_injr", "insights": []}
        ]}}


def test_insights():
    result = client.execute("""query { insights { id, title, entityId, valueType }}""")
    assert result == {"data": {"insights": [ 
        {"id": "BII", "title": "Bodily Injury Identification", "entityId": "claim_part", "valueType": "float"}, 
        {"id": "TL", "title": "Total Loss", "entityId": "claim_asset", "valueType": "float"}
        ]}}


def test_insights_resolved_entity():
    result = client.execute("""query { insights { id, entity { id } }}""")
    assert result == {"data": {"insights": [ 
        {"id": "BII", "entity" : { "id": "claim_part" }}, 
        {"id": "TL", "entity" : { "id": "claim_asset" }}
        ]}}


def test_insights_resolved_models():
    result = client.execute("""query { insights { id, models { id } }}""")
    assert result == {"data": {"insights": [ 
        {"id": "BII", "models" : [{ "id": "m1" }, { "id": "m2" }]}, 
        {"id": "TL", "models" : [{ "id": "m3" }]}
        ]}}


def test_models():
    result = client.execute("""query { models { id, title, insightId }}""")
    assert result == {"data": {"models": [ 
        {"id": "m1", "title": "M1 for BII", "insightId": "BII"}, 
        {"id": "m2", "title": "M2 for BII", "insightId": "BII"},
        {"id": "m3", "title": "M3 for TL", "insightId": "TL"}
        ]}}


def test_models_resolved_entity():
    result = client.execute("""query { models { id, insight { id } } }""")
    assert result == {"data": {"models": [ 
        {"id": "m1", "insight": { "id": "BII"}}, 
        {"id": "m2", "insight": { "id": "BII"}},
        {"id": "m3", "insight": { "id": "TL"}}
        ]}}

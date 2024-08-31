import json
entity_data = {}

def setup():
    global entity_data

    with open('./data/entity.json', 'r') as file:
        _entities = json.load(file)
        entity_data = dict([(_e["id"], _e) for _e in _entities])

def get_entity(id):
    return entity_data.get(id)

def get_entities():
    return entity_data.values()

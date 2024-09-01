import json
_entity_data = {}
_insight_data = {}

def setup(path="./data/"):
    global _entity_data
    global _insight_data

    with open(f'{path}entity.json', 'r') as file:
        _entities = json.load(file)
        _entity_data = dict([(_e["id"], _e) for _e in _entities])

    with open(f'{path}insight.json', 'r') as file:
        _insights = json.load(file)
        _insight_data = dict([(_e["id"], _e) for _e in _insights])

def get_entity(id):
    return _entity_data.get(id)

def get_entities():
    return _entity_data.values()

def get_entity_children(id):
    return [_entity_data.get(k) for k,v in _entity_data.items() if "parents" in v and id in [a['entity_id'] for a in v['parents']]]

def get_insight(id):
    return _insight_data.get(id)

def get_insights():
    return _insight_data.values()

def get_entity_insights(id):
    return [_insight_data.get(k) for k,v in _insight_data.items() if id == v['entity_id']]

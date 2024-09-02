import json
_entity_data = {}
_insight_data = {}
_model_data = {}

def setup(path="./data/"):
    global _entity_data
    global _insight_data
    global _model_data

    with open(f'{path}entity.json', 'r') as file:
        _entities = json.load(file)
        _entity_data = dict([(_e["id"], _e) for _e in _entities])

    with open(f'{path}insight.json', 'r') as file:
        _insights = json.load(file)
        _insight_data = dict([(_e["id"], _e) for _e in _insights])

    with open(f'{path}model.json', 'r') as file:
        _models = json.load(file)
        _model_data = dict([(_e["id"], _e) for _e in _models])

def get_entity(id):
    return _entity_data.get(id)

def get_entities():
    return _entity_data.values()

def get_entity_children(id):
    return [_entity_data.get(k) for k,v in _entity_data.items() if "belongs_to" in v and id in [a['entity_id'] for a in v['belongs_to']]]

def get_entity_belongs_to(id):
    entity = _entity_data.get(id)
    if 'belongs_to' in entity:
       return [_entity_data.get(p['entity_id']) for p in entity['belongs_to']]
    return []

def get_insight(id):
    return _insight_data.get(id)

def get_insights():
    return _insight_data.values()

def get_insights_by_entity_id(entity_id):
    return [v for k,v in _insight_data.items() if entity_id == v['entity_id']]

def get_model(id):
    return _model_data.get(id)

def get_models():
    return _model_data.values()

def get_models_by_insight_id(insight_id):
    return [v for k,v in _model_data.items() if v['insight_id'] == insight_id]

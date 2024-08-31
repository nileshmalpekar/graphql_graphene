entity_data = {}

def setup():
    from schema import Entity

    global entity_data

    claim = Entity(id="claim", title="Claim")
    claim_part = Entity(id="claim_part", title="Claim Participant")

    entity_data = {
        claim.id: claim,
        claim_part.id: claim_part
    }

def get_entity(id):
    return entity_data.get(id)

def get_entities():
    return entity_data.values()

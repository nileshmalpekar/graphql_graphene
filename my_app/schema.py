import graphene

# from graphene_mongo import MongoengineObjectType

# from models import User as UserModel
from .data import *

# class User(MongoengineObjectType):
#     class Meta:
#         model = UserModel
#     full_name = graphene.String()
#     def resolve_full_name(self, info):
#         return f"{self.first_name} {self.last_name}"

class EntityParent(graphene.ObjectType):
    entity_id = graphene.ID()
    foreign_key = graphene.List(graphene.NonNull(graphene.String))

    entity = graphene.Field(lambda: Entity)

    def resolve_entity(parent, info):
        return get_entity(parent['entity_id'])

class Entity(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    primary_key = graphene.List(graphene.NonNull(graphene.String))
    belongs_to = graphene.List(graphene.NonNull(EntityParent))

    children_entities = graphene.List(graphene.NonNull(lambda: Entity))
    parent_entities = graphene.List(graphene.NonNull(lambda: Entity))
    insights = graphene.List(lambda: Insight)

    def resolve_children_entities(parent, info):
        return list(get_entity_children(parent['id']))

    def resolve_parent_entities(parent, info):
        return list(get_entity_belongs_to(parent['id']))

    def resolve_insights(parent, info):
        return list(get_insights_by_entity_id(parent['id']))

class Insight(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    value_type = graphene.String(required=True)
    entity_id = graphene.ID(required=True)

    entity = graphene.Field(lambda: Entity)
    models = graphene.List(lambda: Model)

    def resolve_entity(parent, info):
        return get_entity(parent['entity_id'])
    
    def resolve_models(parent, info):
        return get_models_by_insight_id(parent['id'])

class Model(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    insight_id = graphene.ID(required=True)
    
    insight = graphene.Field(lambda: Insight)

    def resolve_insight(parent, info):
        return get_insight(parent['insight_id'])


class Query(graphene.ObjectType):
    # users = graphene.List(User)

    entities = graphene.List(Entity)
    entity = graphene.Field(Entity, id=graphene.String())

    def resolve_entity(root, info, id):
        return get_entity(id)
    
    def resolve_entities(self, info):
        return list(get_entities())

    # def resolve_users(self, info):
    #     return list(UserModel.objects.all())

    insights = graphene.List(Insight)
    insight = graphene.Field(Insight, id=graphene.String())

    def resolve_insight(root, info, id):
        return get_insight(id)
    
    def resolve_insights(self, info):
        return list(get_insights())

    models = graphene.List(Model)
    model = graphene.Field(Model, id=graphene.String())

    def resolve_model(root, info, id):
        return get_model(id)
    
    def resolve_models(self, info):
        return list(get_models())

schema = graphene.Schema(query=Query)

import graphene

# from graphene_mongo import MongoengineObjectType

# from models import User as UserModel
import data

# class User(MongoengineObjectType):
#     class Meta:
#         model = UserModel
#     full_name = graphene.String()
#     def resolve_full_name(self, info):
#         return f"{self.first_name} {self.last_name}"

class EntityParent(graphene.ObjectType):
    entity_id = graphene.ID()
    entity = graphene.Field(lambda: Entity)
    foreign_key = graphene.List(graphene.NonNull(graphene.String))

    def resolve_entity(parent, info):
        return data.get_entity(parent['entity_id'])

class Entity(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    primary_key = graphene.List(graphene.NonNull(graphene.String))
    parents = graphene.List(graphene.NonNull(EntityParent))
    children = graphene.List(graphene.NonNull(lambda: Entity))

    def resolve_children(parent, info):
        return list(data.get_entity_children(parent['id']))

class Query(graphene.ObjectType):
    # users = graphene.List(User)

    entities = graphene.List(Entity)
    entity = graphene.Field(Entity, id=graphene.String())

    def resolve_entity(root, info, id):
        return data.get_entity(id)
    
    def resolve_entities(self, info):
        return list(data.get_entities())

    # def resolve_users(self, info):
    #     return list(UserModel.objects.all())


schema = graphene.Schema(query=Query)

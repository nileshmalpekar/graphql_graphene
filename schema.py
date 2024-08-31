import graphene

from graphene_mongo import MongoengineObjectType

from models import User as UserModel


class User(MongoengineObjectType):
    class Meta:
        model = UserModel
    full_name = graphene.String()
    def resolve_full_name(self, info):
        return f"{self.first_name} {self.last_name}"

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return list(UserModel.objects.all())


schema = graphene.Schema(query=Query)

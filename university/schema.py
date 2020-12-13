import graphene
from api.schema import Query as queries


class Query(queries, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

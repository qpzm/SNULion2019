import graphene

import feeds.schema

class Query(feeds.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

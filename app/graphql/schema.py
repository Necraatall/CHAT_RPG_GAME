import graphene
from ..schemas.item import Query as ItemQuery, Mutation as ItemMutation
from ..schemas.extracted_text import Query as ExtractedTextQuery, Mutation as ExtractedTextMutation
from ..schemas.character import Query as CharacterQuery, Mutation as CharacterMutation

class Query(ItemQuery, ExtractedTextQuery, CharacterQuery, graphene.ObjectType):
    pass

class Mutation(ItemMutation, ExtractedTextMutation, CharacterMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

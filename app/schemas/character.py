import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from ..models.character import Character as CharacterModel
from ..database import SessionLocal

class Character(SQLAlchemyObjectType):
    class Meta:
        model = CharacterModel

class Query(graphene.ObjectType):
    characters = graphene.List(Character)

    def resolve_characters(self, info):
        query = Character.get_query(info)
        return query.all()

class CreateCharacter(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        health = graphene.Int()
        money = graphene.Int()
        race = graphene.String()
        class_type = graphene.String()

    ok = graphene.Boolean()
    character = graphene.Field(lambda: Character)

    def mutate(self, info, name, health, money, race, class_type):
        db = SessionLocal()
        character = CharacterModel(name=name, health=health, money=money, race=race, class_type=class_type)
        db.add(character)
        db.commit()
        db.refresh(character)
        ok = True
        return CreateCharacter(character=character, ok=ok)

class Mutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()

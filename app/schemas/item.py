import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from ..models.item import Item as ItemModel
from ..database import SessionLocal

class Item(SQLAlchemyObjectType):
    class Meta:
        model = ItemModel

class Query(graphene.ObjectType):
    items = graphene.List(Item)

    def resolve_items(self, info):
        query = Item.get_query(info)
        return query.all()

class CreateItem(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()

    ok = graphene.Boolean()
    item = graphene.Field(lambda: Item)

    def mutate(self, info, name, description):
        db = SessionLocal()
        item = ItemModel(name=name, description=description)
        db.add(item)
        db.commit()
        db.refresh(item)
        ok = True
        return CreateItem(item=item, ok=ok)

class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()

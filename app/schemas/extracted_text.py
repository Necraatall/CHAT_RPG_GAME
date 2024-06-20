import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from ..models.extracted_text import ExtractedText as ExtractedTextModel
from ..database import SessionLocal

class ExtractedText(SQLAlchemyObjectType):
    class Meta:
        model = ExtractedTextModel

class Query(graphene.ObjectType):
    extracted_text = graphene.List(ExtractedText)

    def resolve_extracted_text(self, info):
        query = ExtractedText.get_query(info)
        return query.all()

class CreateExtractedText(graphene.Mutation):
    class Arguments:
        page_number = graphene.Int()
        text = graphene.String()

    ok = graphene.Boolean()
    extracted_text = graphene.Field(lambda: ExtractedText)

    def mutate(self, info, page_number, text):
        db = SessionLocal()
        extracted_text = ExtractedTextModel(page_number=page_number, text=text)
        db.add(extracted_text)
        db.commit()
        db.refresh(extracted_text)
        ok = True
        return CreateExtractedText(extracted_text=extracted_text, ok=ok)

class Mutation(graphene.ObjectType):
    create_extracted_text = CreateExtractedText.Field()

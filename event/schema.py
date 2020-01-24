import graphene
from graphene_django.types import DjangoObjectType
from .models import Event, Partner, Product


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class PartnerType(DjangoObjectType):
    class Meta:
        model = Partner


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class Query(graphene.AbstractType):
    all_event = graphene.List(EventType)

    all_partner = graphene.List(PartnerType)

    all_product = graphene.List(ProductType)

    event = graphene.Field(EventType,
                           id=graphene.Int())

    partner = graphene.Field(PartnerType,
                             id=graphene.Int())

    product = graphene.Field(ProductType,
                             id=graphene.Int())

    def resolve_all_event(self, context, **kwargs):
        return Event.objects.all()

    def resolve_event(self, context, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Event.objects.get(pk=id)
        return None

    def resolve_all_partner(self, context, **kwargs):
        return Partner.objects.all()

    def resolve_partner(self, context, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Partner.objects.get(pk=id)
        return None

    def resolve_all_product(self, context, **kwargs):
        return Product.objects.all()

    def resolve_product(self, context, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Product.objects.get(pk=id)
        return None


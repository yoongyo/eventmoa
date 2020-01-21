import graphene
from graphene_django.types import DjangoObjectType
from .models import Event, Partner


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class PartnerType(DjangoObjectType):
    class Meta:
        model = Partner


class Query(graphene.AbstractType):
    all_event = graphene.List(EventType)

    all_partner = graphene.List(PartnerType)

    event = graphene.Field(EventType,
                              id=graphene.Int())

    partner = graphene.Field(PartnerType,
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



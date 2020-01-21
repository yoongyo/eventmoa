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

    def resolve_all_event(self, context, **kwargs):
        return Event.objects.all()

    def resolve_all_partner(self, context, **kwargs):
        return Partner.objects.all()

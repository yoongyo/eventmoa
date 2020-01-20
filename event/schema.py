import graphene
from graphene_django.types import DjangoObjectType
from .models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class Query(graphene.AbstractType):
    all_event = graphene.List(EventType)

    def resolve_all_event(self, context, **kwargs):
        return Event.objects.all()

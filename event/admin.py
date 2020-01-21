from django.contrib import admin
from .models import Event, HashTag, Partner


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'partner']


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name']


class HashTagAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(HashTagAdmin, HashTag)
admin.site.register(EventAdmin, Event)
admin.site.regitser(PartnerAdmin, Partner)

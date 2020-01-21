from django.contrib import admin
from .models import Event, HashTag, Partner


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'partner']


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['partner']


class HashTagAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(HashTag, HashTagAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Partner, PartnerAdmin)

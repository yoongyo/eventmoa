from django.contrib import admin
from .models import Event, HashTag, Partner


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'partner']


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name']


class HashTagAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(HashTag, HashTagAdmin)
admin.site.register(Event, EventAdmin)
admin.site.regitser(Partner, PartnerAdmin)

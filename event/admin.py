from django.contrib import admin
from .models import Event, HashTag, Partner, Product


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'partner']


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name']


class HashTagAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(HashTag, HashTagAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Partner, PartnerAdmin)

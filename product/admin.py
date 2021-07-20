from django.contrib import admin
from . import models


class VariationInline(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'short_description', 
        'get_price_formated',
        'get_price_promotional_formated',
    )
    list_display_links = ('name',)
    inlines = [
        VariationInline
    ]


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Variation)

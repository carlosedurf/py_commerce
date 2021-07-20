from django.contrib import admin
from . import models


class VariationInline(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        VariationInline
    ]


admin.register(models.Product, ProductAdmin)
admin.register(models.Variation)

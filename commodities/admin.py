from django.contrib import admin
from . import models

# Register your models here.


class CommodityImageInline(admin.StackedInline):
    model = models.CommodityImage


@admin.register(models.Commodity)
class CommodityAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price')
    inlines = (CommodityImageInline,)




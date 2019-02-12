from django.contrib import admin
from apps.scraper.models import Element, Tag, Attribute, Value, Refer


# Register your models here.
class ValueInline(admin.StackedInline):
    model = Value
    extra = 1


class ReferAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


class ElementAdmin(admin.ModelAdmin):
    inlines = (
        ValueInline,
    )
    list_display = ('pk', 'refers', 'tag')


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Refer, ReferAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Tag, TagAdmin)

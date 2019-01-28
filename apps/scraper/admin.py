from django.contrib import admin
from apps.scraper.models import Element, Tag, Attribute, Value

# Register your models here.
class ValueInline(admin.StackedInline):
    model = Value
    extra = 1


class ElementAdmin(admin.ModelAdmin):
	inlines = (
		ValueInline,
	)

class AttributeAdmin(admin.ModelAdmin):
	pass

class TagAdmin(admin.ModelAdmin):
	pass

admin.site.register(Element, ElementAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Tag, TagAdmin)
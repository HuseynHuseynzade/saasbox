from django.contrib import admin
from core.models import Slider, Feature


class SliderAdmin(admin.ModelAdmin):
    list_display = ('heading', 'title', 'order',)
    list_editable = ('order',)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'percent', 'order',)
    # fields = ('title','percent')
    list_editable = ('order',)


admin.site.register(Slider, SliderAdmin)
admin.site.register(Feature, FeatureAdmin)

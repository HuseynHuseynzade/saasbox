from django.contrib import admin
from core.models import Slider


class SliderAdmin(admin.ModelAdmin):
    list_display = ('heading', 'title', 'order')
    list_editable = ('order',)


admin.site.register(Slider, SliderAdmin)

from django.contrib import admin

# Register your models here.
from services.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


admin.site.register(Service, ServiceAdmin)

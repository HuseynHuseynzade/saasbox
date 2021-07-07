from django.contrib import admin

# Register your models here.
from services.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','text', 'order', 'chk')
    list_editable = ('order', 'chk')

#admin
admin.site.register(Service, ServiceAdmin)

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from core.views import BaseContext
from services.models import Service


class ServiceView(BaseContext, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        services = Service.objects.all().order_by('-order')

        context.update({'services': services})
        return context

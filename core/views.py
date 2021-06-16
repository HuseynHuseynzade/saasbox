from django.shortcuts import render

# Create your views here.
from django.views.generic.base import ContextMixin, TemplateView
from services.models import Service
from core.models import Slider, Feature


class BaseContext(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class IndexView(BaseContext, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        sliders = Slider.objects.all().order_by('order')
        services = Service.objects.filter(chk=True).order_by('order')[:3]
        features = Feature.objects.all().order_by('order')[:3]

        context.update({'sliders': sliders, 'services': services, 'features': features})
        return context


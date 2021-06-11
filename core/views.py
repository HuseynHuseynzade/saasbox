from django.shortcuts import render

# Create your views here.
from django.views.generic.base import ContextMixin, TemplateView

from core.models import Slider


class BaseContext(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class IndexView(BaseContext, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        sliders = Slider.objects.all().order_by('order')

        context.update({'sliders': sliders})
        return context

from django.views.generic import TemplateView
from django.http import JsonResponse

class Main(TemplateView):
    template_name = 'index.html'

from django.views.generic import TemplateView
from wiki.models import Module, View, Knowledge
from django.template.loader import render_to_string
from django.http import JsonResponse
from wiki.forms import *


class Main(TemplateView):
    template_name = 'index.html'

    def search(request):
        text = request.GET['text']
        model = request.GET['model']

        if model == 'moduleList':
            modules = Module.objects.filter(name__icontains=text)
            result = render_to_string('module_list.html', {'modules': modules})
            return JsonResponse({'result': result})

        elif model == 'formList':
            forms = View.objects.filter(name__icontains=text)
            result = render_to_string('form_list.html', {'forms': forms})
            return JsonResponse({'result': result})

        elif model == 'knowledgeList':
            knowledge_list = Knowledge.objects.filter(title__icontains=text)
            result = render_to_string('knowledge_list.html', {'knowledge_list': knowledge_list})
            return JsonResponse({'result': result})

    def get_form(request):
        model = request.GET['model']

        if model == 'knowledgeList':
            form = ErrorForm()
        result = render_to_string('form_for_change.html', {'form': form}, request=request)
        return JsonResponse({'result': result})
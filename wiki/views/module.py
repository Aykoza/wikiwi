from django.core.serializers import serialize
from django.template.loader import render_to_string
from django.views import generic
from wiki.forms import ModuleForm
from wiki.models import Module
from django.http import JsonResponse, Http404


class ModuleList(generic.ListView):
    model = Module
    template_name = 'module_list.html'
    form = ModuleForm

    def get_data(request):
        if request.method == 'GET':
            modules = render_to_string('module_list.html', {'modules': Module.objects.all()})
            return JsonResponse({'modules': modules})
        else:
            raise Http404('Post request ERROR!')

    def get_module(request):
        if request.method == 'GET':
            module = render_to_string('module.html', {'module': Module.objects.filter(id=request.GET['id'])[0]})
            return JsonResponse({'module': module})
        else:
            raise Http404('Post request ERROR!')
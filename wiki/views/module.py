from django.template.loader import render_to_string
from django.views import generic
from wiki.forms import ModuleForm
from wiki.models import Module
from django.http import JsonResponse, request, Http404


class ModuleList(generic.ListView):
    model = Module
    template_name = 'error_list.html'
    form = ModuleForm

    def get_data(self):
        if request.method == 'POST':
            content = {'modules': Module.objects.all()}
            content = render_to_string('error_list.html', content)
            return JsonResponse({'modules': content})
        else:
            raise Http404('Post request ERROR!')

    # def get_context_data(self, **kwargs):
    #     context = super(ModuleList, self).get_context_data(**kwargs)
    #     context['error_list'] = Module.objects.all()
    #     context['form'] = self.form
    #     return context

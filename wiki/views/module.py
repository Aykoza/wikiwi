from django.views import generic
from wiki.forms import ModuleForm
from wiki.models import Module


class ModuleList(generic.ListView):
    model = Module
    template_name = 'error_list.html'
    form = ModuleForm

    def get_context_data(self, **kwargs):
        context = super(ModuleList, self).get_context_data(**kwargs)
        context['error_list'] = Module.objects.all()
        context['form'] = self.form
        return context

from django.http import JsonResponse, Http404
from django.template.loader import render_to_string
from django.views import generic
from wiki.forms import ErrorForm
from wiki.models import Knowledge


class KnowledgeList(generic.ListView):
    model = Knowledge
    template_name = 'knowledge_list.html'
    form = ErrorForm

    def get_context_data(self, **kwargs):
        context = super(Knowledge, self).get_context_data(**kwargs)
        context['error_list'] = Knowledge.objects.all()
        context['form'] = self.form
        return context

    def get_data(request):
        if request.method == 'GET':
            knowledge_list = render_to_string('knowledge_list.html', {'knowledge_list': Knowledge.objects.all()})
            # modules = serialize('json', Module.objects.all())
            return JsonResponse({'knowledge_list': knowledge_list})
        else:
            raise Http404('Post request ERROR!')
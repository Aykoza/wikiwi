from django.views import generic
from wiki.forms import ViewForm
from wiki.models import View
from django.template.loader import render_to_string
from django.http import JsonResponse, Http404


class ViewList(generic.ListView):
    model = View
    template_name = 'form_list.html'
    form = ViewForm

    def get_context_data(self, **kwargs):
        context = super(ViewList, self).get_context_data(**kwargs)
        context['error_list'] = View.objects.all()
        context['form'] = self.form
        return context

    def get_data(request):
        if request.method == 'GET':
            forms = render_to_string('form_list.html', {'forms': View.objects.all()})
            # modules = serialize('json', Module.objects.all())
            return JsonResponse({'forms': forms})
        else:
            raise Http404('Post request ERROR!')
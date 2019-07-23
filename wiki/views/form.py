from django.views import generic
from wiki.forms import ViewForm
from wiki.models import View


class ViewList(generic.ListView):
    model = View
    template_name = 'error_list.html'
    form = ViewForm

    def get_context_data(self, **kwargs):
        context = super(ViewList, self).get_context_data(**kwargs)
        context['error_list'] = View.objects.all()
        context['form'] = self.form
        return context

from django.views import generic
from wiki.forms import ErrorForm
from wiki.models import Error


class ErrorList(generic.ListView):
    model = Error
    template_name = 'error_list.html'
    form = ErrorForm

    def get_context_data(self, **kwargs):
        context = super(ErrorList, self).get_context_data(**kwargs)
        context['error_list'] = Error.objects.all()
        context['form'] = self.form
        return context
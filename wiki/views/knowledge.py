from django.http import JsonResponse, Http404
from django.template.loader import render_to_string
from django.views import generic
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from wiki.forms import ErrorForm, AttachmentForm
from wiki.models import Knowledge, Attachment
from .main import Main


class KnowledgeList(View):
    model = Knowledge
    template_name = 'knowledge_list.html'
    # form = ErrorForm

    def get_context_data(self, **kwargs):
        context = super(KnowledgeList, self).get_context_data(**kwargs)
        context['error_list'] = Knowledge.objects.all()
        context['form'] = self.form
        return context

    def get_data(request=None):
        knowledge_list = render_to_string('knowledge_list.html', {'knowledge_list': Knowledge.objects.all()})
        return JsonResponse({'knowledge_list': knowledge_list})

    def get_knowledge(request):
        if request.method == 'GET':
            knowledge = Knowledge.objects.filter(id=request.GET['id'])[0]
            attachments = Attachment.objects.filter(knowledge=request.GET['id'])
            result = render_to_string('knowledge.html', {'knowledge': knowledge, 'attachments': attachments})
            return JsonResponse({'knowledge': result})
        else:
            raise Http404('Post request ERROR!')

    def save_knowledge(self, request):
        if request.method == 'POST':
            form = ErrorForm(request.POST)
            if form.is_valid():
                form.save()
                knowledge_list = self.get_data()
                return knowledge_list
        else:
            raise Http404('Post request ERROR!')

    def remove_knowledge(self, request):
        knowledge = Knowledge.objects.filter(id=request.GET['id'])[0]
        knowledge.delete()
        return self.get_data()


class Attachment(CreateView):
    model = Attachment
    form = AttachmentForm
    template_name = 'attachment.html'
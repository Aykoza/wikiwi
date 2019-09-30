from django.urls import path
from wiki.views.knowledge import KnowledgeList
from wiki.views.module import ModuleList
from wiki.views.form import ViewList
from wiki.views.main import Main

urlpatterns = [
    path('', Main.as_view(), name='index'),
    path('modules/', ModuleList.get_data, name='modules'),
    path('module/', ModuleList.get_module, name='module'),
    path('forms/', ViewList.get_data, name='forms'),
    path('form/', ViewList.get_view, name='form'),
    path('knowledge_list/', KnowledgeList.get_data, name='knowledge_list'),
    path('knowledge/', KnowledgeList.get_knowledge, name='knowledge'),
    path('views/', ViewList.as_view(), name='views'),
    path('search/', Main.search, name='search'),
    path('get_form/', Main.get_form, name='get_add_element_form'),
    path('save_knowledge/', KnowledgeList().save_knowledge, name='save_knowledge'),
    path('remove_knowledge/', KnowledgeList().remove_knowledge, name='remove_knowledge')
    # path('errors/', KnowledgeList.as_view(), name='knowledge'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
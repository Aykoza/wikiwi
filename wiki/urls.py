from django.urls import path
from wiki.views.knowledge import KnowledgeList
from wiki.views.module import ModuleList
from wiki.views.form import ViewList
from wiki.views.main import Main

urlpatterns = [
    path('', Main.as_view(), name='index'),
    path('modules/', ModuleList.get_data, name='modules'),
    path('forms/', ViewList.get_data, name='forms'),
    path('form/', ViewList.get_view, name='form'),
    path('knowledge/', KnowledgeList.get_data, name='knowledge'),
    path('views/', ViewList.as_view(), name='views'),
    path('search/', ViewList.as_view(), name='views'),
    # path('errors/', KnowledgeList.as_view(), name='knowledge'),
]
from django.urls import path
from wiki.views import e

urlpatterns = [
    path('/', ErrorList.as_view(), name='index'),
]
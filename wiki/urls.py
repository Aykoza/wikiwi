from django.urls import path
from wiki.views.error import ErrorList

urlpatterns = [
    path('', ErrorList.as_view(), name='index'),
]
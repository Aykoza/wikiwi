from django import forms
from .models import Error, Module, View


class ModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ['name']


class ViewForm(forms.ModelForm):

    class Meta:
        model = View
        fields = ['name', 'name_view', 'module', 'type', 'description']


class ErrorForm(forms.ModelForm):

    class Meta:
        model = Error
        fields = ['title', 'view', 'description', 'decision', 'attachment']
from django import forms
from .models import Error


class ErrorForm(forms.ModelForm):

    class Meta:
        model = Error
        fields = ['title', 'view', 'description', 'decision', 'attachment']
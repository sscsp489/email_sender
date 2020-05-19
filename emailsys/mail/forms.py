from django import forms
from .models import emails,mess

class mailForm(forms.ModelForm):
    class Meta:
        model = emails
        fields = [
            'mail',
        ]

class messForm(forms.ModelForm):
    class Meta:
        model = mess
        fields = [
            'message',
            'subject'
        ]
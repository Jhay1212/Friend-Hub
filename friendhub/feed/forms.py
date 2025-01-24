from django import forms
# from django.forms.
from .models import Chirp


class ChirpForm(forms.Form):
    user = forms.CharField(min_length=1, max_length=12 )
    contenta = forms.Textarea()
    def save(self):
        pass
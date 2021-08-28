from django import forms
from django.forms import ModelForm

from .models import Person


class Triangle(forms.Form):
    kat1 = forms.IntegerField(label="leg 1", min_value=1)
    kat2 = forms.IntegerField(label="leg 2", min_value=1)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']

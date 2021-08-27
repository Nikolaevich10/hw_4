from django import forms


class Triangle(forms.Form):
    kat1 = forms.IntegerField(label="leg 1", min_value=1)
    kat2 = forms.IntegerField(label="leg 2", min_value=1)

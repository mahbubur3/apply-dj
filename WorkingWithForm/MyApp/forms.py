from django import forms


class NameForm(forms.Form):
    first_name = forms.CharField(label="First Name: ")
    last_name = forms.CharField(label="Last Name: ")

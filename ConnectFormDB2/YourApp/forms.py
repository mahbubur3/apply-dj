from django import forms
from YourApp import models


class CarForm(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = "__all__"

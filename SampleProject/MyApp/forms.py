from django import forms
from MyApp import models


class ActorForm(forms.ModelForm):
    class Meta:
        model = models.Actor
        fields = "__all__"


class MovieForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Movie
        fields = "__all__"

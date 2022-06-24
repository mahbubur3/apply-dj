from django import forms
from MyApp import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"

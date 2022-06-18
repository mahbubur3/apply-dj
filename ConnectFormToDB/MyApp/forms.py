from django import forms
from django.core import validators
from MyApp.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

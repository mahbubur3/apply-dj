from django import forms
from django.core import validators


# def even_or_not(value):
#     if value % 2 != 0:
#         raise forms.ValidationError("Please insert and even number.")


# class UserForm(forms.Form):
#     number_field = forms.IntegerField(validators=[even_or_not])


# class UserForm(forms.Form):
# field = forms.CharField(validators=[
#     validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])

# number_field = forms.IntegerField(
#     validators=[validators.MaxValueValidator(10), validators.MinValueValidator(5)])


class UserForm(forms.Form):
    user_password = forms.IntegerField(label='Password')
    entered_password = forms.IntegerField(label='Your password')

    def clean(self):
        all_cleaned_data = super().clean()
        user_pass = all_cleaned_data['user_password']
        entered_pass = all_cleaned_data['entered_password']

        if user_pass != entered_pass:
            raise forms.ValidationError('password does not match!!')

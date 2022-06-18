from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(label="Name: ", widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your name',
            'style': 'background-color: yellow',
        }))
    email = forms.EmailField(label="Email: ", widget=forms.TextInput(
        attrs={'placeholder': 'Enter your email'}))
    password = forms.IntegerField(label="Password", widget=forms.TextInput(
        attrs={'placeholder': 'Enter your password'}))

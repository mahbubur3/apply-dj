from django import forms


class InfoForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={'placeholder': 'Enter your name', 'style': 'width: 200px'}
    ))
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'placeholder': 'Enter your email', 'style': 'width: 200px'}
    ))
    dob = forms.DateField(label='Date of Birth', widget=forms.TextInput(
        attrs={'style': 'width: 200px', 'type': 'date'}
    ))
    address = forms.CharField(label='Address', widget=forms.TextInput(
        attrs={'placeholder': 'Enter your address', 'style': 'width: 200px'}
    ))

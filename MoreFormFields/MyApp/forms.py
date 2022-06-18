from django import forms


class InfoForm(forms.Form):
    field = forms.CharField(label='name', max_length=10, min_length=4)

    # choice field
    # field_two = forms.ChoiceField(label='choose', choices=(
    #     ('', 'SELECT OPTION'),
    #     ('1', 'first'),
    #     ('2', 'second'),
    #     ('3', 'third')
    # ))

    options = (
        ('', 'SELECT OPTION'),
        ('1', 'first'),
        ('2', 'second'),
        ('3', 'third')
    )
    field_two = forms.ChoiceField(choices=options)

    # bolean field
    field_three = forms.BooleanField(label='YES OR NO')

    # choice field with radioselect
    brands = (
        ('1', 'Apple'),
        ('2', 'Samsung'),
        ('3', 'Google')
    )
    field_four = forms.ChoiceField(
        label='Select your favorite brand..', choices=brands, widget=forms.RadioSelect)

    # multiple choice field with checkbox
    products = (
        ('1', 'Watch'),
        ('2', 'Charger'),
        ('3', 'Keyboard'),
        ('4', 'Mouse')
    )
    field_five = forms.MultipleChoiceField(
        label='select your products..', choices=products, widget=forms.CheckboxSelectMultiple)

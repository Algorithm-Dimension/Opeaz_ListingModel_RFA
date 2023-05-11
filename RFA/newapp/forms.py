from django import forms

class FiltresForm(forms.Form):
    FILTRE_CHOICES = (
        ('CA', 'Chiffre d\'affaires'),
        ('Benefice', 'Bénéfice'),
    )
    OPERATOR_CHOICES = (
        ('lt', '<'),
        ('gt', '>'),
        ('eq', '='),
    )

    filtre1 = forms.ChoiceField(choices=FILTRE_CHOICES)
    filtre2 = forms.ChoiceField(choices=OPERATOR_CHOICES)
    nombre = forms.IntegerField()
    date1 = forms.DateField(input_formats=['%Y-%m-%d'], help_text='Format attendu : YYYY-MM-DD')
    date2 = forms.DateField(input_formats=['%Y-%m-%d'], help_text='Format attendu : YYYY-MM-DD')

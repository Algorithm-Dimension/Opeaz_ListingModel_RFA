from django import forms


class ConditionForm(forms.Form):
    FILTRE_CHOICES = (
        ('CA', 'Chiffre d\'affaires'),
        ('Benefice', 'Bénéfice'),
    )
    OPERATOR_CHOICES = (
        ('lt', '<'),
        ('gt', '>'),
        ('eq', '='),
    )

    conditions = forms.IntegerField(min_value=1, max_value=5, label='Nombre de conditions')

    def generate_condition_fields(self, conditions_count):
        self.fields.clear()  # Supprimer tous les champs existants

        for i in range(1, conditions_count + 1):
            self.fields[f'filtre{i}'] = forms.ChoiceField(choices=self.FILTRE_CHOICES, label=f'Filtre {i}')
            self.fields[f'operateur{i}'] = forms.ChoiceField(choices=self.OPERATOR_CHOICES, label=f'Opérateur {i}')
            self.fields[f'valeur{i}'] = forms.FloatField(label=f'Valeur {i}')
            self.fields[f'date1{i}'] = forms.DateField(input_formats=['%Y-%m-%d'],
                                                       help_text='Format attendu : YYYY-MM-DD', label=f'Date 1 {i}')
            self.fields[f'date2{i}'] = forms.DateField(input_formats=['%Y-%m-%d'],
                                                       help_text='Format attendu : YYYY-MM-DD', label=f'Date 2 {i}')

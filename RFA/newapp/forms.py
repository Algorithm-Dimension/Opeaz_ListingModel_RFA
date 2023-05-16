from django import forms
from django.forms import ModelForm, DateInput

from django import forms
from django.forms import ModelForm
from .models import Condition
from django.core.validators import MinValueValidator, MaxValueValidator


class DateInput(forms.DateInput):
    input_type = 'date'


class ConditionForm(ModelForm):

    class Meta:
        model = Condition
        fields = '__all__'
        # fields = ['what', 'who', 'operator', 'unit', 'start_date', 'end_date']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }

class EntireConditionForm(forms.Form):
    condition = forms.CharField(label='Entrez votre ensemble de conditions')

class ConditionNumberForm(forms.Form):
    condition_number = forms.IntegerField(label='Nombre de conditions',
                                          validators=[
                                              MinValueValidator(1, message='Veuillez entrer au moins une condition'),
                                              MaxValueValidator(5, message='Vous ne pouvez entrer plus de 5 conditions'),
                                          ]
                                          )


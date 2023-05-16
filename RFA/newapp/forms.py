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
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }

    def add_prefix(self, field_name):
        return f'{field_name}_1'



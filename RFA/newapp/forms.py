from django import forms
from django.forms import ModelForm, DateInput

from django import forms
from django.forms import ModelForm
from .models import SimpleCondition, ComparativeCondition
from django.core.validators import MinValueValidator, MaxValueValidator


class DateInput(forms.DateInput):
    input_type = 'date'


class SimpleConditionForm(ModelForm):

    class Meta:
        model = SimpleCondition
        fields = '__all__'
        widgets = {
            # 'what': forms.Select(attrs={'class': 'what'}),
            'start_date': DateInput(),
            'end_date': DateInput()
        }


class ComparativeConditionForm(ModelForm):

    class Meta:
        model = ComparativeCondition
        fields = '__all__'
        widgets = {
            'first_start_date': DateInput(),
            'first_end_date': DateInput(),
            'second_start_date': DateInput(),
            'second_end_date': DateInput()
        }

    def add_prefix(self, field_name):
        return f'comp_{field_name}_1'






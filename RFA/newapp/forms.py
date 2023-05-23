from django import forms
from django.forms import ModelForm, DateInput

from django import forms
from django.forms import ModelForm
from .models import SimpleCondition, ComparativeCondition, Pharmacy, NoCondition
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

    def add_prefix(self, field_name):
        return f'simple_{field_name}'


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
        return f'comp_{field_name}'


class NoConditionForm(ModelForm):

    class Meta:
        model = NoCondition
        fields = '__all__'
        widgets = {
            # 'what': forms.Select(attrs={'class': 'what'}),
            'start_date': DateInput(),
            'end_date': DateInput()
        }

    def add_prefix(self, field_name):
        return f'no_{field_name}'


class PharmaForm(forms.Form):
    TYPE_CHOICES = (
        ('group', 'Group'),
        ('pharma', 'Pharmacie'),
    )

    type = forms.ChoiceField(choices=TYPE_CHOICES, label='TYPE')
    group = forms.ModelChoiceField(queryset=Pharmacy.objects.all().values_list('group', flat=True).distinct(),
                                   label='GROUPE')

    pharmacy = forms.ModelChoiceField(queryset=Pharmacy.objects.all().values_list('pharma_name', flat=True).distinct(),
                                      label='PHARMACIE')

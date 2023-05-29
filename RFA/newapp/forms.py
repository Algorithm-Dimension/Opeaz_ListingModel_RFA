from django import forms
from django.forms import ModelForm, DateInput

from django import forms
from django.forms import ModelForm
from .models import SimpleCondition, ComparativeCondition, Pharmacy, NoCondition
from django.core.validators import MinValueValidator, MaxValueValidator

from .serializers import PharmacySerializer


class DateInput(forms.DateInput):
    input_type = 'date'


class SimpleConditionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['subtype'].choices = self.get_type_choices()
        for field_name in self.fields:
            if field_name != 'who':
                self.fields[field_name].required = True

    def get_type_choices(self):
        type_choices = Pharmacy.objects.values_list('subtype', 'subtype').distinct()
        return type_choices

    class Meta:
        model = SimpleCondition
        fields = '__all__'

    def add_prefix(self, field_name):
        return f'simple_{field_name}'


class ComparativeConditionForm(ModelForm):

    class Meta:
        model = ComparativeCondition
        fields = '__all__'


    def add_prefix(self, field_name):
        return f'comp_{field_name}'


class NoConditionForm(ModelForm):

    class Meta:
        model = NoCondition
        fields = '__all__'

    def add_prefix(self, field_name):
        return f'no_{field_name}'


class PharmaForm(forms.Form):
    TYPE_CHOICES = (
        ('group', 'Group'),
        ('pharma', 'Pharmacie'),
    )

    pharmas = Pharmacy.objects.all()
    serialized_data = PharmacySerializer(pharmas, many=True).data
    group_choices = set(item['group'] for item in serialized_data)
    pharma_choices = set(item['pharma_name'] for item in serialized_data)

    type = forms.ChoiceField(choices=TYPE_CHOICES, label='TYPE')
    group = forms.ChoiceField(choices=[(choice, choice) for choice in group_choices], label='GROUPE')

    pharmacy = forms.ChoiceField(choices=[(choice, choice) for choice in pharma_choices], label='PHARMACIE')

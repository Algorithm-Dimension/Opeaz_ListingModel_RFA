from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.forms import ModelForm, DateInput


from .models import Pharmacy
# Create your views here.


def home(request):
    print(1)
    return HttpResponse("Hello World")


def home(request):
    return render(request, 'index.html')

from django.shortcuts import render
from .forms import ConditionForm, ConditionNumberForm, EntireConditionForm


def filtres_page(request):
    condition_number_form = ConditionNumberForm(request.POST or None)
    rfa = None
    cond_forms = []

    if request.method == 'POST' and condition_number_form.is_valid():
        for i in range(condition_number_form.cleaned_data['condition_number']):
            cond_forms.append(ConditionForm(prefix=f'Condition {i}'))

    entire_condition_form = EntireConditionForm()
    # return render(request, 'filtres.html', {'form': form, 'subforms': subforms, 'rfa': rfa})
    return render(request, 'cond_2.html', {'forms': cond_forms, 'condition_number_form': condition_number_form,
                                            'entire_form': entire_condition_form, 'n':len(cond_forms)})


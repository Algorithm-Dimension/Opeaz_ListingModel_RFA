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
from .forms import ConditionForm


def filtres_page(request):
    condition_form = ConditionForm()
    condition_forms = [condition_form]

    return render(request, 'filtres.html', {'forms': condition_forms, 'cond_form':condition_form})


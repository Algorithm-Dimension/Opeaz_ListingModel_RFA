from django.http import HttpResponse
from django.shortcuts import render
from .forms import SimpleConditionForm, ComparativeConditionForm
from .models import Pharmacy
# Create your views here.


def home(request):
    print(1)
    return HttpResponse("Hello World")


def home(request):
    return render(request, 'index.html')


def filtres_page(request):
    simple_condition_form = SimpleConditionForm()
    comparative_condition_form = ComparativeConditionForm()
    condition_forms = [simple_condition_form]

    return render(request, 'filtres2.html', {'forms': condition_forms, 'simple_condition_form': simple_condition_form,
                                            'comparative_condition_form': comparative_condition_form})


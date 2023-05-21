from django.http import HttpResponse
from django.shortcuts import render
from .forms import SimpleConditionForm, ComparativeConditionForm, PharmaForm, NoConditionForm
from .models import Pharmacy
# Create your views here.


def home(request):
    return HttpResponse("Hello World")


def home(request):
    return render(request, 'index.html')


def filtres_page(request):
    pharma_form = PharmaForm()
    simple_condition_form = SimpleConditionForm()
    comparative_condition_form = ComparativeConditionForm()
    no_condition_form = NoConditionForm()

    return render(request, 'filtres.html', {
                                            'simple_condition_form': simple_condition_form,
                                            'comparative_condition_form': comparative_condition_form,
                                            'pharma_form': pharma_form,
                                            'no_condition_form': no_condition_form,
                                            }
                  )


from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Hello World")


def home(request):
    return render(request, 'index.html')

from django.shortcuts import render
from .forms import ConditionForm

def filtres_page(request):
    form = ConditionForm(request.POST or None)
    rfa = None
    subforms = []

    if request.method == 'POST' and form.is_valid():
        conditions_count = form.cleaned_data['conditions']

        if conditions_count < 1 or conditions_count > 5:
            form.add_error('conditions', 'Le nombre de conditions doit être compris entre 1 et 5.')
        else:
            subforms = []
            for i in range(1, conditions_count + 1):
                subform = ConditionForm(prefix=f'condition_{i}')
                subform.generate_condition_fields(1)
                subforms.append(subform)

            # Effectuer le traitement des formulaires icii
            # ...

    return render(request, 'filtres.html', {'form': form, 'subforms': subforms, 'rfa': rfa})

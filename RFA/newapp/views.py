from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Hello World")


def home(request):
    return render(request, 'index.html')




from django.shortcuts import render
from .forms import FiltresForm

def filtres_page(request):
    form = FiltresForm()
    rfa = None

    if request.method == 'POST':
        form = FiltresForm(request.POST)

        if form.is_valid():
            filtre1 = form.cleaned_data['filtre1']
            filtre2 = form.cleaned_data['filtre2']
            nombre = form.cleaned_data['nombre']
            date1 = form.cleaned_data['date1']
            date2 = form.cleaned_data['date2']

            if filtre1 == 'CA' and filtre2 == 'lt' and nombre > 0 and date1 < date2:
                rfa = 50
            elif filtre1 == 'Benefice' and filtre2 == 'gt' and nombre > 0 and date1 < date2:
                rfa = 50

    return render(request, 'filtres.html', {'form': form, 'rfa': rfa})


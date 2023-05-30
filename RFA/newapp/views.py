import re

from django.http import HttpResponse
from django.shortcuts import render
from .forms import SimpleConditionForm, ComparativeConditionForm, PharmaForm, NoConditionForm
from .models import Pharmacy
from .serializers import PharmacySerializer, SubtypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return HttpResponse("Hello World")


def home(request):
    return render(request, 'index.html')


class PharmaListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        http://127.0.0.1:8000/api/pharma/?name=Ternes&group=GROUP1&ca__gt=70
        Pour voir les pharma avec ca > 70
        '''
        data = {k: v for k, v in request.GET.items()}
        pharmas = Pharmacy.objects.filter(**data)
        serializer = PharmacySerializer(pharmas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubtypeListApiView(APIView):
    def get(self, request, subtype):
        pharmas = Pharmacy.objects.filter(type=subtype)
        serializer = SubtypeSerializer(pharmas, many=True)
        data = set(d['subtype'] for d in serializer.data)
        return Response(data, status=status.HTTP_200_OK)


def filtres_page(request):
    pharma_form = PharmaForm()
    simple_condition_form = SimpleConditionForm()
    comparative_condition_form = ComparativeConditionForm()
    no_condition_form = NoConditionForm()

    if request.POST:
        conditions_number = max([int(re.findall(r'\d+', k)[0]) for k in request.POST if re.findall(r'\d+', k)])
        base_condition = {'pharma_name': request.POST.get('pharmacy')} if 'pharmacy' in request.POST \
            else {'group': request.POST.get('group')}
        pharmas, rfa = set(), 0
        for i in range(conditions_number):
            condition = {}
            data = {k.split('_')[1]: v for k, v in request.POST.items() if k.endswith(f'{i + 1}')}
            if any('simple' in k for k in request.POST if k.endswith(f'{i + 1}')):
                condition = base_condition | get_simple_condition_data(data)
            if any('comp' in k for k in request.POST if k.endswith(f'{i + 1}')):
                condition = base_condition | get_comparative_condition_data(data)
            if data.get('type') == 'ET':
                pharmas = list(pharmas & set([p.pharma_name for p in Pharmacy.objects.filter(**condition)]))
            elif data.get('type') == 'OU':
                pharmas = list(pharmas | set([p.pharma_name for p in Pharmacy.objects.filter(**condition)]))
            else:
                pharmas = set([p.pharma_name for p in Pharmacy.objects.filter(**condition)])
            rfa = max(rfa, int(data.get('rate', 0)))
            print(request.POST)
        return render(request, 'results.html', {'rfa': rfa if pharmas else None})

    return render(request, 'filtres.html', {
                                            'simple_condition_form': simple_condition_form,
                                            'comparative_condition_form': comparative_condition_form,
                                            'pharma_form': pharma_form,
                                            'no_condition_form': no_condition_form,
                                            }
                  )


def get_simple_condition_data(data):
    what = data.get("what", "").lower()
    operator = data.get("operator", "")
    return {f'{what}__{operator}' if operator != 'eq' else what: data.get("quantity", ""),
            "year": data.get("year", ""),
            'subtype': data.get("subtype", "")}


def get_comparative_condition_data(data):
    what = data.get("what", "").lower()
    operator = data.get("operator", "")
    return {f'{what}_evolution__{operator}' if operator != 'eq' else f'{what}_evolution': data.get("quantity", ""),
            "year": max(data.get("first"), data.get('second')),
            'subtype': data.get("subtype", "")}


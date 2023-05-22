from django.http import HttpResponse
from django.shortcuts import render
from .forms import SimpleConditionForm, ComparativeConditionForm, PharmaForm, NoConditionForm
from .models import Pharmacy
from .serializers import PharmacySerializer
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


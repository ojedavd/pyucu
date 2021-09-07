from django.shortcuts import render
from django.db.models import Q
from .models import Certificado


def index(request):
    queryset = request.GET.get("buscar")  
    certificados = []

    if queryset:
        certificados = Certificado.objects.filter(dni = queryset)


    return render(request, 'certificados/index.html', {'latest_question_list': certificados})


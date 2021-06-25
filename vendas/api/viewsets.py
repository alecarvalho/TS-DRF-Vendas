
import json
import requests
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VendaSerializer, VendaItensSerializer
from vendas.models import Vendas, VendaItens, Vendas



# api_url_base = 'http://127.0.0.1:8888/'


def home(request):
   response = requests.get('http://127.0.0.1:8888/product/')
   data = response.json()
   venda = Vendas.objects.all()
   return render(request, 'home.html', {'data': data,'venda': venda })


class VendasViewSet(viewsets.ModelViewSet):
    queryset = Vendas.objects.all()
    serializer_class = VendaSerializer

class VendaItensViewSet(viewsets.ModelViewSet):
    queryset = VendaItens.objects.all()
    serializer_class = VendaItensSerializer


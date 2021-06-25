
from rest_framework.fields import ModelField
from vendas.models import Vendas, VendaItens
from rest_framework import serializers


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendas
        fields = '__all__'

class VendaItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendaItens
        fields = '__all__'
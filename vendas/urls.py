from requests.api import patch
from rest_framework.routers import DefaultRouter
from django.urls import path
from vendas.api.viewsets import VendasViewSet, VendaItensViewSet, home

router = DefaultRouter()


router.register('vendas', VendasViewSet, basename='vendas')
router.register('vendas_itens', VendaItensViewSet, basename='vendas_itens')

urlpatterns = router.urls

urlpatterns_home = [

    path('', home, name="home"),
]
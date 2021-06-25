from django.db import models
from django.db.models.deletion import CASCADE


class Vendas(models.Model):
    seller_id = models.IntegerField()
    buyer_id = models.IntegerField()
    marketplace = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.id}'

class VendaItens(models.Model):
    product_id = models.IntegerField()
    venda_id = models.ForeignKey(Vendas, on_delete=CASCADE, related_name='venda_itens')
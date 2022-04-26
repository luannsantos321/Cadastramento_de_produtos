from django.db import models

# Create your models here.

class Cadastramento(models.Model):
    nome_produto = models.CharField(max_length=100,  verbose_name='Nome do produto')
    valor = models.DecimalField(decimal_places=2, max_digits=7)
    validade = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de criação')

    class Meta:
        db_table = 'cadastramento'''
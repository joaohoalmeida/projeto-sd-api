from django.db import models

# Create your models here.

class Caminhao(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=100)
    capacidade_kg = models.IntegerField()
    ativo = models.BooleanField(default=True)

class Motorista(models.Model):
    cnh = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

class Frete(models.Model):
    STATUS = [
        ('TRANSITO', 'Trânsito'),
        ('CONCLUIDO', 'Concluido'),
    ]

    motorista = models.ForeignKey(Motorista, on_delete=models.PROTECT, related_name='Fretes')
    caminhao = models.ForeignKey(Caminhao, on_delete=models.PROTECT, related_name='Fretes')

    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    data_saida = models.DateField(auto_now_add=True)
    data_entrega = models.DateField(null=True, blank=True, default=None)

    status = models.CharField(max_length=10, choices=STATUS)
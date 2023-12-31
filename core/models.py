from django.db import models

    
class Stand(models.Model):
    localizacao = models.CharField(max_length=150)
    valor = models.FloatField()

    def __str__(self):
        return self.localizacao
    
class Reserva(models.Model):
    cnpj = models.CharField(max_length=11)
    nome_empresa = models.CharField(max_length=150)
    categoria_empresa = models.CharField(max_length=150)
    quitado = models.BooleanField(default=False)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Reserva")
        verbose_name_plural = ("Reservas")

    def __str__(self):
        return self.nome_empresa
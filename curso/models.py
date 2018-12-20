from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=150, null=False, verbose_name="Nome do Curso")
    qtd_vagas = models.IntegerField(null=False, verbose_name="Quantidade de Vagas")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Curso'
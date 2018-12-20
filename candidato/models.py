from django.contrib.auth.models import User
from django.db import models

class Candidato(models.Model):
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )
    nome = models.CharField(max_length=150, null=False, verbose_name="Nome do Candidato", blank=True)
    cpf = models.CharField(max_length=11, verbose_name="CPF", blank=True)
    endereco = models.CharField(max_length=200, null=False, verbose_name="Endereço", blank=True)
    matricula = models.CharField(max_length=25, verbose_name="Matrícula", blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, verbose_name="Sexo", blank=True)
    dta_nascimento = models.DateField(null=False, verbose_name="Data de Nascimento", blank=True)
    curriculo = models.FileField(upload_to='uploads/', blank=True)
    celular = models.CharField(max_length=15, null=False, verbose_name="Celular", blank=True)
    usuario = models.OneToOneField(User, related_name="candidato", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Candidatos'  
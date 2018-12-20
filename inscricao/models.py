from django.db import models
from candidato.models import Candidato
from evento.models import Evento
from curso.models import Curso

class Inscricao(models.Model):
    candidato = models.ForeignKey(Candidato, related_name="inscricao", on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, related_name="evento", on_delete=models.CASCADE, blank=True)
    curso = models.ForeignKey(Curso, related_name="curso", on_delete=models.CASCADE, blank=True)
    dta_inscricao = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Inscrições'
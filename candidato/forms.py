from django.forms import ModelForm

from .models import Candidato

class CandidatoForm(ModelForm):
    class Meta:
        model = Candidato
    #    fields = "__all__"
        exclude = ['usuario']

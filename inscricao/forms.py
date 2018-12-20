from django.forms import ModelForm
from .models import Inscricao

class InscricaoForm(ModelForm):
    class Meta:
        model = Inscricao
#       fields = "__all__"
        exclude = ['candidato']
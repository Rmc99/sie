from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Inscricao, Curso
from .forms import InscricaoForm
from django.contrib import messages

@login_required
def efetuar_inscricao(request):
    form = InscricaoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            inscricao = form.save(commit=False)
            inscricao.candidato = request.user.candidato
            vagas = vaga_por_curso(request, inscricao.curso)
            cursos = Curso.objects.get(nome=inscricao.curso)
            print('cursos.qtd_vagas-->', cursos.qtd_vagas)
            if vagas <= cursos.qtd_vagas:
                inscricao.save()
                messages.success(request, 'Inscrição confirmada no curso')
                return redirect('candidato:dashboard')
            else:
                messages.info(request, 'Vagas já preenchidas')
    return render(request, 'efetuar_inscricao.html', {'form': form, 'usuario_logado': request.user})

def vaga_por_curso(request, curso_escolhido):
    query = Inscricao.objects.filter(curso=curso_escolhido).count()
    print('Query-->', query)
    return query


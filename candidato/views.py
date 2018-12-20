from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CandidatoForm
from django.contrib import messages
from .models import Candidato, User

@login_required
def dashboard(request):
    usuario = User.objects.get(pk=request.user.id)
    try:
        lista_candidato = Candidato.objects.get(usuario=usuario.id)
    #    lista_candidato = get_object_or_404(Candidato, usuario=usuario.id)
        return render(request, 'dashboard.html',
                      {'lista': lista_candidato, 'usuario_logado': request.user})
    except Candidato.DoesNotExist:
        return redirect('candidato:cadastro_candidato')

@login_required
def cadastro_candidato(request):
    form = CandidatoForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            candidato = form.save(commit=False)
            candidato.usuario = request.user
            candidato.save()
            messages.success(request, 'Operação realizada com sucesso!')
            # PASSAR PARAMETRO NO REDIRECT
            # return redirect('candidato:dashboard', pk=candidato.pk)
            return redirect('candidato:dashboard')
    return render(request, 'cadastro_candidato.html', {'form': form, 'usuario_logado': request.user})

@login_required
def atualiza_candidato(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)

    form = CandidatoForm(request.POST or None, request.FILES or None, instance=candidato)

    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('candidato:dashboard')
    return render(request, 'atualiza_candidato.html', {'form': form, 'usuario_logado': request.user})
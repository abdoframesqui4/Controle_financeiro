from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoriaForm, ContaForm, DespesaForm, MetaForm, ReceitaForm
from .models import Categoria, Conta, Despesa, MetaEconomia, Receita


# ---------------------------------------------------------------
# Página inicial: resumo das finanças
# ---------------------------------------------------------------
def inicio(request):
    total_receitas = sum(r.valor for r in Receita.objects.all())
    total_despesas = sum(d.valor for d in Despesa.objects.all())

    contexto = {
        "total_receitas": total_receitas,
        "total_despesas": total_despesas,
        "saldo": total_receitas - total_despesas,
        "contas": Conta.objects.all(),
        "metas": MetaEconomia.objects.all(),
        "ultimas_despesas": Despesa.objects.order_by("-data")[:5],
    }
    return render(request, "financas/inicio.html", contexto)


# ---------------------------------------------------------------
# Funções genéricas reaproveitadas por todas as tabelas
# ---------------------------------------------------------------
def formulario(request, classe_form, titulo, voltar_para, objeto=None):
    """Mostra o formulário e salva quando ele é enviado (criar ou editar)."""
    if request.method == "POST":
        form = classe_form(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return redirect(voltar_para)
    else:
        form = classe_form(instance=objeto)

    contexto = {"form": form, "titulo": titulo, "voltar_para": voltar_para}
    return render(request, "financas/formulario.html", contexto)


def excluir(request, objeto, voltar_para):
    """Pede confirmação e apaga o registro."""
    erro = None
    if request.method == "POST":
        try:
            objeto.delete()
            return redirect(voltar_para)
        except ProtectedError:
            # Ex.: categoria que ainda está sendo usada em receitas/despesas
            erro = "Não é possível excluir: este registro está sendo usado em outro lugar."

    contexto = {"objeto": objeto, "voltar_para": voltar_para, "erro": erro}
    return render(request, "financas/excluir.html", contexto)


# ---------------------------------------------------------------
# Categorias
# ---------------------------------------------------------------
def categoria_lista(request):
    categorias = Categoria.objects.order_by("nome")
    return render(request, "financas/categoria_lista.html", {"categorias": categorias})


def categoria_nova(request):
    return formulario(request, CategoriaForm, "Nova categoria", "categoria_lista")


def categoria_editar(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    return formulario(request, CategoriaForm, "Editar categoria", "categoria_lista", categoria)


def categoria_excluir(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    return excluir(request, categoria, "categoria_lista")


# ---------------------------------------------------------------
# Contas
# ---------------------------------------------------------------
def conta_lista(request):
    contas = Conta.objects.order_by("nome")
    return render(request, "financas/conta_lista.html", {"contas": contas})


def conta_nova(request):
    return formulario(request, ContaForm, "Nova conta", "conta_lista")


def conta_editar(request, id):
    conta = get_object_or_404(Conta, id=id)
    return formulario(request, ContaForm, "Editar conta", "conta_lista", conta)


def conta_excluir(request, id):
    conta = get_object_or_404(Conta, id=id)
    return excluir(request, conta, "conta_lista")


# ---------------------------------------------------------------
# Receitas
# ---------------------------------------------------------------
def receita_lista(request):
    receitas = Receita.objects.order_by("-data")
    return render(request, "financas/receita_lista.html", {"receitas": receitas})


def receita_nova(request):
    return formulario(request, ReceitaForm, "Nova receita", "receita_lista")


def receita_editar(request, id):
    receita = get_object_or_404(Receita, id=id)
    return formulario(request, ReceitaForm, "Editar receita", "receita_lista", receita)


def receita_excluir(request, id):
    receita = get_object_or_404(Receita, id=id)
    return excluir(request, receita, "receita_lista")


# ---------------------------------------------------------------
# Despesas
# ---------------------------------------------------------------
def despesa_lista(request):
    despesas = Despesa.objects.order_by("-data")
    return render(request, "financas/despesa_lista.html", {"despesas": despesas})


def despesa_nova(request):
    return formulario(request, DespesaForm, "Nova despesa", "despesa_lista")


def despesa_editar(request, id):
    despesa = get_object_or_404(Despesa, id=id)
    return formulario(request, DespesaForm, "Editar despesa", "despesa_lista", despesa)


def despesa_excluir(request, id):
    despesa = get_object_or_404(Despesa, id=id)
    return excluir(request, despesa, "despesa_lista")


# ---------------------------------------------------------------
# Metas de economia
# ---------------------------------------------------------------
def meta_lista(request):
    metas = MetaEconomia.objects.order_by("prazo")
    return render(request, "financas/meta_lista.html", {"metas": metas})


def meta_nova(request):
    return formulario(request, MetaForm, "Nova meta", "meta_lista")


def meta_editar(request, id):
    meta = get_object_or_404(MetaEconomia, id=id)
    return formulario(request, MetaForm, "Editar meta", "meta_lista", meta)


def meta_excluir(request, id):
    meta = get_object_or_404(MetaEconomia, id=id)
    return excluir(request, meta, "meta_lista")

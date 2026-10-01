from django import forms

from .models import Categoria, Conta, Despesa, MetaEconomia, Receita

# Faz o campo de data aparecer como calendário no navegador
CAMPO_DATA = forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d")


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome", "tipo"]


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ["nome", "banco", "saldo_inicial"]


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ["descricao", "valor", "data", "categoria", "conta"]
        widgets = {"data": CAMPO_DATA}


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ["descricao", "valor", "data", "pago", "categoria", "conta"]
        widgets = {"data": CAMPO_DATA}


class MetaForm(forms.ModelForm):
    class Meta:
        model = MetaEconomia
        fields = ["nome", "valor_objetivo", "valor_guardado", "prazo"]
        widgets = {"prazo": CAMPO_DATA}

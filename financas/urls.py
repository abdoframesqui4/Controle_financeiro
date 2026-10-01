from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),

    path("categorias/", views.categoria_lista, name="categoria_lista"),
    path("categorias/nova/", views.categoria_nova, name="categoria_nova"),
    path("categorias/<int:id>/editar/", views.categoria_editar, name="categoria_editar"),
    path("categorias/<int:id>/excluir/", views.categoria_excluir, name="categoria_excluir"),

    path("contas/", views.conta_lista, name="conta_lista"),
    path("contas/nova/", views.conta_nova, name="conta_nova"),
    path("contas/<int:id>/editar/", views.conta_editar, name="conta_editar"),
    path("contas/<int:id>/excluir/", views.conta_excluir, name="conta_excluir"),

    path("receitas/", views.receita_lista, name="receita_lista"),
    path("receitas/nova/", views.receita_nova, name="receita_nova"),
    path("receitas/<int:id>/editar/", views.receita_editar, name="receita_editar"),
    path("receitas/<int:id>/excluir/", views.receita_excluir, name="receita_excluir"),

    path("despesas/", views.despesa_lista, name="despesa_lista"),
    path("despesas/nova/", views.despesa_nova, name="despesa_nova"),
    path("despesas/<int:id>/editar/", views.despesa_editar, name="despesa_editar"),
    path("despesas/<int:id>/excluir/", views.despesa_excluir, name="despesa_excluir"),

    path("metas/", views.meta_lista, name="meta_lista"),
    path("metas/nova/", views.meta_nova, name="meta_nova"),
    path("metas/<int:id>/editar/", views.meta_editar, name="meta_editar"),
    path("metas/<int:id>/excluir/", views.meta_excluir, name="meta_excluir"),
]

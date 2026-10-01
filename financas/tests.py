from django.test import TestCase

from .models import Categoria, Conta, MetaEconomia


class TestesBasicos(TestCase):
    def setUp(self):
        self.client.post("/categorias/nova/", {"nome": "Salário", "tipo": "R"})
        self.client.post("/categorias/nova/", {"nome": "Mercado", "tipo": "D"})
        self.client.post("/contas/nova/", {"nome": "Nubank", "banco": "Nu", "saldo_inicial": "100"})

    def test_paginas_abrem(self):
        for url in ["/", "/categorias/", "/contas/", "/receitas/", "/despesas/", "/metas/"]:
            self.assertEqual(self.client.get(url).status_code, 200)

    def test_saldo_da_conta(self):
        categoria_r = Categoria.objects.get(nome="Salário")
        categoria_d = Categoria.objects.get(nome="Mercado")
        conta = Conta.objects.get(nome="Nubank")
        self.client.post("/receitas/nova/", {"descricao": "Salário", "valor": "3000", "data": "2026-10-01",
                                              "categoria": categoria_r.id, "conta": conta.id})
        self.client.post("/despesas/nova/", {"descricao": "Compras", "valor": "250.50", "data": "2026-10-01",
                                              "pago": "on", "categoria": categoria_d.id, "conta": conta.id})
        self.assertEqual(conta.saldo_atual(), 2849.50)

    def test_porcentagem_da_meta(self):
        meta = MetaEconomia.objects.create(nome="Viagem", valor_objetivo=5000, valor_guardado=1250, prazo="2027-06-01")
        self.assertEqual(meta.porcentagem(), 25)

    def test_nao_exclui_categoria_em_uso(self):
        categoria = Categoria.objects.get(nome="Salário")
        conta = Conta.objects.get(nome="Nubank")
        self.client.post("/receitas/nova/", {"descricao": "Salário", "valor": "10", "data": "2026-10-01",
                                              "categoria": categoria.id, "conta": conta.id})
        resposta = self.client.post(f"/categorias/{categoria.id}/excluir/")
        self.assertContains(resposta, "Não é possível excluir")
        self.assertTrue(Categoria.objects.filter(id=categoria.id).exists())

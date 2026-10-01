from django.db import models


# Tabela 1: Categoria (ex.: Alimentação, Salário, Transporte)
class Categoria(models.Model):
    TIPOS = [
        ("R", "Receita"),
        ("D", "Despesa"),
    ]

    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=TIPOS)

    def __str__(self):
        return self.nome


# Tabela 2: Conta (ex.: Carteira, Banco do Brasil, Nubank)
class Conta(models.Model):
    nome = models.CharField(max_length=50)
    banco = models.CharField(max_length=50, blank=True)
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.nome

    def saldo_atual(self):
        """Saldo inicial + todas as receitas - todas as despesas da conta."""
        total_receitas = sum(r.valor for r in self.receitas.all())
        total_despesas = sum(d.valor for d in self.despesas.all())
        return self.saldo_inicial + total_receitas - total_despesas


# Tabela 3: Receita (dinheiro que entra)
class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name="receitas")

    def __str__(self):
        return self.descricao


# Tabela 4: Despesa (dinheiro que sai)
class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    pago = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name="despesas")

    def __str__(self):
        return self.descricao


# Tabela 5: Meta (objetivo de economia, ex.: Viagem, Reserva de emergência)
class MetaEconomia(models.Model):
    nome = models.CharField(max_length=100)
    valor_objetivo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_guardado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prazo = models.DateField()

    class Meta:
        verbose_name = "Meta de economia"
        verbose_name_plural = "Metas de economia"

    def __str__(self):
        return self.nome

    def porcentagem(self):
        """Quanto da meta já foi alcançado (0 a 100)."""
        if self.valor_objetivo == 0:
            return 0
        resultado = self.valor_guardado / self.valor_objetivo * 100
        return min(int(resultado), 100)

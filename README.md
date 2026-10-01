# Controle Financeiro (Django)

Sistema simples de controle financeiro feito em Django, com código fácil de entender.

## As 5 tabelas (em `financas/models.py`)

| Tabela | Para que serve | Campos |
|---|---|---|
| **Categoria** | Agrupar lançamentos (Salário, Mercado...) | nome, tipo (Receita/Despesa) |
| **Conta** | Onde o dinheiro está (Carteira, Banco...) | nome, banco, saldo_inicial |
| **Receita** | Dinheiro que entra | descricao, valor, data, categoria, conta |
| **Despesa** | Dinheiro que sai | descricao, valor, data, pago, categoria, conta |
| **MetaEconomia** | Objetivos de economia (Viagem...) | nome, valor_objetivo, valor_guardado, prazo |

## Como rodar

```bash
# 1. (opcional) criar ambiente virtual
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. instalar o Django
pip install -r requirements.txt

# 3. criar o banco de dados
python manage.py migrate

# 4. (opcional) criar usuário para o painel /admin
python manage.py createsuperuser

# 5. iniciar o servidor
python manage.py runserver
```

Acesse **http://127.0.0.1:8000/**

> Dica: cadastre primeiro uma **Categoria** e uma **Conta**, porque Receitas e Despesas precisam delas.

## Estrutura dos arquivos

```
config/                 -> configurações do projeto (settings.py, urls.py)
financas/
├── models.py           -> as 5 tabelas
├── forms.py            -> formulários de cadastro
├── views.py            -> lógica das páginas
├── urls.py             -> endereços (rotas) das páginas
├── admin.py            -> registra as tabelas no /admin
├── tests.py            -> testes automáticos (python manage.py test)
├── templates/financas/ -> páginas HTML
└── static/financas/    -> estilo.css
```

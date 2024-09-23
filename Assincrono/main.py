import time
import random
from faker import Faker
import asyncio

# Inicializa o Faker para gerar nomes aleatórios
fake = Faker()

# Lista de nomes aleatórios
nomes = [fake.name() for _ in range(1000)]

# Dicionário para armazenar os dados de vendas
vendas = {}

# Preenche o dicionário com nomes aleatórios e vendas aleatórias
for nome in nomes:
    vendas[nome] = random.randint(100, 10000)  # Vendas aleatórias entre 100 e 10000

# Exibe um exemplo de como ficaria o dicionário com alguns elementos
exemplo_dicionario = {k: vendas[k] for k in list(vendas)[:3]}  # Exibe os primeiros 3 elementos





async def calcula_imposto(faturamento):
    print(f"Valor do imposto: {faturamento * 0.1}")




async def calcular_bonus_funcionarios(vendas):
    for funcionario, venda in vendas.items():
        bonus = venda * 0.05
        print(f"{funcionario} - Bônus: {bonus}")
        time.sleep(1)

async def fechamento(vendas):
    tarefa1 = asyncio.create_task(calcular_bonus_funcionarios(vendas))
    tarefa2 = asyncio.create_task(calcula_imposto(sum(vendas.values())))
    print("Fechamento finalizado.")

asyncio.run(fechamento(vendas))

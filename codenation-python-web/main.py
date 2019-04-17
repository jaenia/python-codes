# coding: utf-8
import csv
import heapq

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
def q_1():
    with open('data.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        quantity = [line['nationality'] for line in reader]
        return len(list(set(quantity)))

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    with open('data.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        quantity = [line['club'] for line in reader]
        return len(list(set(quantity)))

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    with open('data.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        return [line['full_name'] for line in reader][0:20]

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    with open('data.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        wages = [(line['full_name'], float(line['eur_wage'])) for line in reader]
        higher_wages = heapq.nlargest(10, wages, key=lambda x: x[1])
        return [name for name, wage in higher_wages]

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    with open('data.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        ages = [(line['full_name'], int(line['age'])) for line in reader]
        higher_ages = heapq.nlargest(10, ages, key=lambda x: x[1])
        return [name for name, age in higher_ages]

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    with open('data.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        ages = [int(line['age']) for line in reader]
        return {age:ages.count(age) for age in set(ages)}

"""
Lucas Gameiro Borges
Vinícius Brito Bastos Antunes
"""

from pulp import *
from matplotlib import *
from numpy import dot

# Questão 1

"""Construindo as variáveis pertinentes"""
x = [LpVariable("Galões do tipo "+str(i+1), lowBound=0, cat="Continuous") for i in range(4)]
    
"""Definindo o problema"""
prob = LpProblem("Lucro da vinícola", LpMaximize)
    
"""Estabelecendo objetivo"""
L = dot([6, 12, 20, 30], x)
    
"""Restringindo o problema"""
r1 = dot([1/3, 1, 2, 10/3], x) <= 50000
r2 = dot([1/2, 1/2, 1, 3/2], x) <= 32000
r3 = dot([0.2, 0.3, 0.3, 0.5], x) <= 12000
    
"""Contabilizando tudo"""
prob+=L
prob+=r1
prob+=r2
prob+=r3

"""Extraindo resultados"""
result = prob.solve()
print('{:-<31}'.format(''))
print('{:^31}'.format("Questão 1"))
print('{:-<31}'.format(''))
print("Solução ótima ocorre quando há:")
for var in x:
    print('{:7}'.format(var.value()), var.name)
    
# Questão 2

"""Construindo as variáveis pertinentes"""
x = [LpVariable("Layouts plantados do tipo "+str(i+1), lowBound=0, cat="Integer") for i in range(3)]
    
"""Definindo o problema"""
prob = LpProblem("Lucro da empresa de jardinagem", LpMaximize)
    
"""Estabelecendo objetivo"""
L = dot([50, 30, 60], x)
    
"""Restringindo o problema"""
r1 = dot([30, 10, 20], x) <= 1000
r2 = dot([20, 40, 50], x) <= 800
r3 = dot([4, 3, 2], x) <= 100
    
"""Contabilizando tudo"""
prob+=L
prob+=r1
prob+=r2
prob+=r3

"""Extraindo resultados"""
result = prob.solve()
print('{:-<31}'.format(''))
print('{:^31}'.format("Questão 2"))
print('{:-<31}'.format(''))
print("Solução ótima ocorre quando há:")
for var in x:
    print('{:7}'.format(var.value()), var.name)
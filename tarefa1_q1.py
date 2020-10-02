"""
Lucas Gameiro Borges
Vinícius Brito Bastos Antunes
"""

from pulp import *

# Questão 1

"""Construindo as variáveis pertinentes"""
x1 = LpVariable("Massa de milho em kg", lowBound=0, cat="Continuous")
x2 = LpVariable("Massa de soja em kg", lowBound=0, cat="Continuous")
    
"""Definindo o problema"""
prob = LpProblem("Custo da empresa", LpMinimize)
    
"""Estabelecendo objetivo"""
C = 0.26*x1 + 0.32*x2
    
"""Restringindo o problema"""
r1 = 0.07*x1 + 0.21*x2 >= 0.34
r2 = 0.82*x1 + 0.79*x2 >= 2.64
    
"""Contabilizando tudo"""
prob+=C
prob+=r1
prob+=r2

"""Extraindo resultados"""
result = prob.solve()
print("Solução ótima ocorre quando:")
print(x1.name, "=", x1.value())
print(x2.name, "=", x2.value())
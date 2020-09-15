from pulp import *
from matplotlib import *

"""Construindo as variáveis pertinentes"""
x1 = LpVariable("Tortas de chocolate", lowBound=0, cat="Integer")
x2 = LpVariable("Tortas de morango", lowBound=0, cat="Integer")
x, y=[], []
    
"""Definindo o problema"""
prob = LpProblem("Distribuição de tortas", LpMaximize)
    
"""Estabelecendo objetivo"""
C = 4*x1 + 2*x2
    
"""Restringindo o problema"""
r1 = 20*x1 + 40*x2 <= 480
r2 = 4*x1 + x2 <= 30
    
"""Contabilizando tudo"""
prob+=C
prob+=r1
prob+=r2
    
"""Extraindo resultados"""
result = prob.solve()
print("Solução ótima ocorre quando x1 =", x1.value(), "e x2 =", x2.value())
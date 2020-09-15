from pulp import *
from matplotlib import *

"""Construindo as variáveis pertinentes"""
x1 = LpVariable("Massa da liga 1", lowBound=0, cat="Continuous")
x2 = LpVariable("Massa da liga 2", lowBound=0, cat="Continuous")
x, y=[], []

"""Variando massa final de aço"""
for i in range(1, 51):
    
    """Definindo o problema"""
    prob = LpProblem("Distribuição da liga", LpMinimize)
    
    """Estabelecendo objetivo"""
    C = 0.19*x1 + 0.2*x2
    
    """Restringindo o problema"""
    r1 = 0.025*(x1 + x2) >= 0.02*x1 + 0.025*x2 >= 0.018*(x1 + x2)
    r2 = 0.012*(x1 + x2) >= 0.01*x1 + 0.015*x2 >= 0.009*(x1 + x2)
    r3 = 0.035*(x1 + x2) >= 0.03*x1 + 0.04*x2 >= 0.032*(x1 + x2)
    r4 = x1 + x2 == i
    
    """Contabilizando tudo"""
    prob+=C
    prob+=r1
    prob+=r2
    prob+=r3
    prob+=r4
    
    """Extraindo resultados"""
    result = prob.solve()
    x.append(x1.value())
    y.append(x2.value())

"""Exibindo resultados"""
pyplot.plot(x, y, 'ro')
pyplot.title(prob.name)
pyplot.xlabel(x1.name)
pyplot.ylabel(x2.name)
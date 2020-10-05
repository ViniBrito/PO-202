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

# Questão 3

"""Construindo as variáveis pertinentes"""
m = [LpVariable("variável m"+str(i+1), lowBound=0, cat="Continuous") for i in range(2)]
d = [LpVariable("variável d"+str(i+1), lowBound=0, cat="Continuous") for i in range(2)]
x = [LpVariable("variável x"+str(i+1), lowBound=0, cat="Continuous") for i in range(2)]
y = [LpVariable("variável y"+str(i+1), lowBound=0, cat="Continuous") for i in range(2)]
    
"""Definindo o problema"""
prob = LpProblem("Custo do tratamento de lixo das cidades", LpMinimize)
    
"""Estabelecendo objetivo"""
L = dot([3*30+40, 5*3+30], m) + dot([36*3+40, 42*3+30], d) + dot([5*3, 3*8], x) + dot([9*3, 6*3], y)
    
"""Restringindo o problema"""
r1 = dot([1, 1], m) == 500
r2 = dot([1, 1], d) == 400
r3 = m[0]+d[0] <= 500
r4 = m[1]+d[1] <= 500
r5 = 0.2*m[0]+0.2*d[0] - x[0] - x[1] == 0
r6 = 0.2*m[1]+0.2*d[1] - y[0] - y[1] == 0
r7 =  x[0]+y[0] <= 200
r8 =  x[1]+y[1] <= 200

"""Contabilizando tudo"""
prob+=L
prob+=r1
prob+=r2
prob+=r3
prob+=r4
prob+=r5
prob+=r6
prob+=r7
prob+=r8

"""Extraindo resultados"""
result = prob.solve()
print('{:-<31}'.format(''))
print('{:^31}'.format("Questão 3"))
print('{:-<31}'.format(''))
print("Solução ótima ocorre quando há:")
for var in m:
    print('{:7}'.format(var.value()), var.name)
for var in d:
    print('{:7}'.format(var.value()), var.name)
for var in x:
    print('{:7}'.format(var.value()), var.name)
for var in y:
    print('{:7}'.format(var.value()), var.name)

# Questão 4

"""Construindo as variáveis pertinentes"""
x = [LpVariable("variável x"+str(i+1), lowBound=0, cat="Integer") for i in range(7)]
    
"""Definindo o problema"""
prob = LpProblem("Minimização de efetivo de trabalhador", LpMinimize)
    
"""Estabelecendo objetivo"""
L = dot([1, 1, 1, 1, 1, 1, 1], x)
    
"""Restringindo o problema"""
r1 = dot([1, 0, 0, 1, 1, 1, 1], x) >= 17
r2 = dot([1, 1, 0, 0, 1, 1, 1], x) >= 13
r3 = dot([1, 1, 1, 0, 0, 1, 1], x) >= 15
r4 = dot([1, 1, 1, 1, 0, 0, 1], x) >= 19
r5 = dot([1, 1, 1, 1, 1, 0, 0], x) >= 14
r6 = dot([0, 1, 1, 1, 1, 1, 0], x) >= 16
r7 = dot([0, 0, 1, 1, 1, 1, 1], x) >= 11    
"""Contabilizando tudo"""
prob+=L
prob+=r1
prob+=r2
prob+=r3
prob+=r4
prob+=r5
prob+=r6
prob+=r7

"""Extraindo resultados"""
result = prob.solve()
print('{:-<31}'.format(''))
print('{:^31}'.format("Questão 4"))
print('{:-<31}'.format(''))
print("Solução ótima ocorre quando há:")
for var in x:
    print('{:7}'.format(var.value()), var.name)

# Questão 5a

"""Construindo as variáveis pertinentes"""
c1 = LpVariable("variavel c1", lowBound=0, cat="Integer")
c2 = LpVariable("variavel c2", lowBound=0, cat="Integer")
v = LpVariable("variavel v", lowBound=0, cat="Continuous")
r = LpVariable("variavel r", lowBound=0, cat="Continuous")
    
"""Definindo o problema"""
prob = LpProblem("Custo de projeto habitacional", LpMinimize)
    
"""Estabelecendo objetivo"""
L = 70*c1 + 120*c2 + 0.056*v + 0.135*r
    
"""Restringindo o problema"""
r1 =  70*c1 + 110*c2 + v + r <= 3100000
r2 = 70*c1 + 120*c2 + 0.056*v + 0.135*r <= 20000
r3 = 0.12*70*c1 + 0.12*110*c2 - v <= 0
r4 = 0.07*70*c1 + 0.07*110*c2 - r == 0
r5 =  c1 + c2 >= 180
r6 =  c1 - c2 <= 50

"""Contabilizando tudo"""
prob+=L
prob+=r1
prob+=r2
prob+=r3
prob+=r4
prob+=r5
prob+=r6

"""Extraindo resultados"""
result = prob.solve()
print('{:-<31}'.format(''))
print('{:^31}'.format("Questão 5a"))
print('{:-<31}'.format(''))
print("Solução ótima ocorre quando há:")
print('{:7}'.format(c1.value()), c1.name)
print('{:7}'.format(c2.value()), c2.name)
print('{:7}'.format(v.value()), v.name)
print('{:7}'.format(r.value()), r.name)

# Questão 5b

"""Construindo as variáveis pertinentes"""
c1 = LpVariable("variavel c1", lowBound=0, cat="Integer")
c2 = LpVariable("variavel c2", lowBound=0, cat="Integer")
v = LpVariable("variavel v", lowBound=0, cat="Continuous")
r = LpVariable("variavel r", lowBound=0, cat="Continuous")
    
"""Definindo o problema"""
prob = LpProblem("Casas de projeto habitacional", LpMaximize)
    
"""Estabelecendo objetivo"""
L = c1 + c2
    
"""Restringindo o problema"""
r1 =  70*c1 + 110*c2 + v + r <= 3100000
r2 = 70*c1 + 120*c2 + 0.056*v + 0.135*r <= 20000
r3 = 0.12*70*c1 + 0.12*110*c2 - v <= 0
r4 = 0.07*70*c1 + 0.07*110*c2 - r == 0
r5 =  c1 + c2 >= 180
r6 =  c1 - c2 <= 50

"""Contabilizando tudo"""
prob+=L
prob+=r1
prob+=r2
prob+=r3
prob+=r4
prob+=r5
prob+=r6

"""Extraindo resultados"""
result = prob.solve()
print('{:-<31}'.format(''))
print('{:^31}'.format("Questão 5b"))
print('{:-<31}'.format(''))
print("Solução ótima ocorre quando há:")
print('{:7}'.format(c1.value()), c1.name)
print('{:7}'.format(c2.value()), c2.name)
print('{:7}'.format(v.value()), v.name)
print('{:7}'.format(r.value()), r.name)



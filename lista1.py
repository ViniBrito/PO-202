import pulp

prob = pulp.LpProblem('questao_5', pulp.LpMinimize)

a = pulp.LpVariable('rendimento_1Al', lowBound=0, upBound=1, cat='Continuous')
b = pulp.LpVariable('rendimento_1Ab', lowBound=0, upBound=1, cat='Continuous')
c = pulp.LpVariable('rendimento_2Al', lowBound=0, upBound=1, cat='Continuous')
d = pulp.LpVariable('rendimento_2Ab', lowBound=0, upBound=1, cat='Continuous')
e = pulp.LpVariable('rendimento_3Al', lowBound=0, upBound=1, cat='Continuous')
f = pulp.LpVariable('rendimento_3Ab', lowBound=0, upBound=1, cat='Continuous')

Custo = 8*a + 10*b + 7*c + 6*d + 11*e + 9*f
prob += Custo

A = 12*a + 9*b + 25*c + 20*d + 17*e + 13*f
B = 35*a + 42*b + 18*c + 31*d + 56*e + 49*f
C = 37*a + 53*b + 28*c + 34*d + 29*e + 20*f

prob += (A>=60)
prob += (B>=150)
prob += (C>=125)

print(prob)

resultado = prob.solve()
assert resultado == pulp.LpStatusOptimal

for var in (a, b, c, d, e, f):
	print('rendimentos: {} = {:1.0f}'.format(var.name, var.value()*100))

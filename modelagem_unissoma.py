import sqlite3
import pulp

# importando o banco de dados fornecido pela ONG
conn = sqlite3.connect('dados.db')

cursor = conn.cursor()

# h = numero de escolas, w = numero de anos
w, h = 3, 4;
z = 6;
 
mm = [[0 for x in range(w)] for y in range(h)] 
M = [[[0 for k in range(z)] for x in range(w)] for y in range(h)] 
print(M[0][0][5])


# puxando tabela de inscritos (vulgo matriz mm)
cursor.execute(""" SELECT * FROM formulario_inscricao; """)

for linha in cursor.fetchall(): # linha 4 sao os anos (2 ao 5) 2 -> nono, 5 -> terceiro, linha 3 sao as escolas
    if linha[4] - 2 >= 0 and linha[4] - 2 <= 3 :
        mm[linha[4] - 2][linha[3] - 1]+= 1


# puxando tabela turma
cursor.execute(""" SELECT * FROM turma; """)
t = []
for linha in cursor.fetchall(): 
    t.append((linha[len(linha)-1] - 2, linha[len(linha)-2] -1, ord(linha[1][len(linha[1]) - 1]) - ord('A')))

# print(t)
# puxando tabela aluno (usaremos para obter M, junto da tabela turma)
cursor.execute(""" SELECT * FROM aluno; """)
for linha in cursor.fetchall(): 
    if t[linha[3] - 1][0] < 3:
        M[ t[linha[3] - 1][0] + 1][ t[linha[3] - 1][1] ][ t[linha[3] - 1][2] ] += linha[len(linha)-1]

# puxando tabela parametro (usaremos para puxar as informações de custos)
cursor.execute(""" SELECT * FROM parametro; """)
req = cursor.fetchall()
C = int(req[3][2]) # custo maximo total
ca = int(req[4][2]) # custo por aluno
cp = int(req[5][2]) # custo por professor
ma = int(req[6][2]) # maximo de alunos por turma
np = int(req[7][2]) + int(req[8][2]) # numero de professores por turma

conn.close()

prob = pulp.LpProblem('otimizacao', pulp.LpMaximize)

x = [pulp.LpVariable('X' + str(i), lowBound=0, upBound=1, cat='Integer') for i in range(75)]
y = [pulp.LpVariable('Y' + str(i), lowBound=0, upBound=ma, cat='Integer') for i in range(75)]

prob += sum(y)
prob += (ca*sum(y) + np*cp*sum(x)<= C)
for i in range(75):
    prob += (y[i] >= x[i])
    prob += (y[i] >= M[i%4][i%3][i%6])
    
resultado = prob.solve()
assert resultado == pulp.LpStatusOptimal


for var in x:
	print('valores de x: {} = {:1.0f}'.format(var.name, var.value()))
for var in y:
	print('valores de y: {} = {:1.0f}'.format(var.name, var.value()))


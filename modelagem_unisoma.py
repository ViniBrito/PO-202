import sqlite3
import pulp

# indice do X ou do Y
#i%h -> B(i,z,h)[0]
def B (i, z, h):
    return (int((i - (i%z) - z*h*int(i/(z*h)))/z), int(i/(z*h)), i%z)

# importando o banco de dados fornecido pela ONG
conn = sqlite3.connect('dados.db')

cursor = conn.cursor()

# puxando tabela parametro (usaremos para puxar as informações de custos)
cursor.execute(""" SELECT * FROM parametro; """)
req = cursor.fetchall()
C = int(req[3][2]) # custo maximo total
ca = int(req[4][2]) # custo por aluno
cp = int(req[5][2]) # custo por professor
ma = int(req[6][2]) # maximo de alunos por turma
np = int(req[7][2]) + int(req[8][2]) # numero de professores por turma

# h = numero de escolas, w = numero de anos

# puxando quantidade de escolas
cursor.execute(""" SELECT * FROM escola; """)
w = 0
for linha in cursor.fetchall():
	w+=1

#puxando quantidade de anos ativos
cursor.execute(""" SELECT * FROM serie; """)
h = 0
for linha in cursor.fetchall():
	h+=linha[2]

z = int(int(C/(cp*np))/(w*h))

mm = [[0 for x in range(w)] for y in range(h)] 
M = [[[0 for k in range(z)] for x in range(w)] for y in range(h)] 

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

# puxando tabela aluno (usaremos para obter M, junto da tabela turma)
cursor.execute(""" SELECT * FROM aluno; """)
for linha in cursor.fetchall(): 
    if t[linha[3] - 1][0] < 3:
        M[ t[linha[3] - 1][0] + 1 - linha[len(linha)-2] ][ t[linha[3] - 1][1] ][ t[linha[3] - 1][2] ] += linha[len(linha)-1]



conn.close()

prob = pulp.LpProblem('otimizacao', pulp.LpMaximize)

tv = w*z*h

x = [pulp.LpVariable('X' + str(i), lowBound=0, upBound=1, cat='Integer') for i in range(tv)]
y = [pulp.LpVariable('Y' + str(i), lowBound=0, upBound=ma, cat='Integer') for i in range(tv)]

prob += C*sum(y) - (ca*sum(y) + np*cp*sum(x))
prob += (ca*sum(y) + np*cp*sum(x)<= C)
for i in range(tv):
    prob += (y[i] >= x[i])
    prob += (y[i] >= M[B(i,z,h)[0]][B(i,z,h)[1]][B(i,z,h)[2]])
    prob += (y[i] <= C*x[i])

for j in range(w):
    for i in range(h):
        S = 0
        SS = mm[i][j]
        for k in range(tv):
            if B(k,z,h)[0] == i and B(k,z,h)[1] == j:
                S += y[k]

        for d in range(z):
            SS += M[i][j][d]
        #print(i, j, S, SS)
        prob += (S <= SS)

for i in range(tv):
    for j in range(tv):
        if B(i,z,h)[0] == B(j,z,h)[0] and B(i,z,h)[1] == B(j,z,h)[1] and B(i,z,h)[2] <= B(j,z,h)[2]:
            prob += (x[i] >= x[j])
'''      
for i in range(tv):
    for j in range(tv):
        if M[B(i,z,h)[0]][B(i,z,h)[1]][B(i,z,h)[2]] == 0 and M[B(j,z,h)[0]][B(j,z,h)[1]][B(j,z,h)[2]] == 0:
            if mm[B(i,z,h)[0]][B(i,z,h)[1]] - mm[B(j,z,h)[0]][B(j,z,h)[1]] > 0.25*ma:
                prob += (x[i] >= x[j])
            elif B(i,z,h)[0] < B(j,z,h)[0]:
                prob += (x[i] >= x[j])
            else:
                prob += (x[j] >= x[i])
'''

'''soma = 0
for j in range(w):
    for i in range(h):
        for k in range(z):
            soma += M[i][j][k]
            print(M[i][j][k], end=" ")
        print("|", end = "")
    print("")    
print(soma)

soma = 0
for j in range(w):
    for i in range(h):
        soma += mm[i][j]
        print(mm[i][j], end=" ")
    print("")
print(soma)'''

resultado = prob.solve()
# assert resultado == pulp.LpStatusOptimal

S = 0
for var in x:
	print('valores de x: {} = {:1.0f}'.format(var.name, var.value()))
for var in y:
    S+=var.value()
    print('valores de y: {} = {:1.0f}'.format(var.name, var.value()))

print("Total de alunos em 2021 =",S)

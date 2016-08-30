import random

minimo = int(input('Informe o valor minimo da faixa: '))
maximo = int(input('Informe o valor maximo da faixa: '))


mtr1Li = int(input('Informe a quantidade de linhas da primeira matriz: '))
mtr1Col = int(input('Informe a quantidade de colunas da primeira matriz: '))

mtr2Li = int(input('Informe a quantidade de linhas da segunda matriz: '))
mtr2Col = int(input('Informe a quantidade de colunas da segunda matriz: '))


def gerarMatriz(matrizlinha, matrizColuna, mini, max):
    mtrRetur = [[random.randrange(mini, max) for j in range(matrizColuna)] for i in range(matrizlinha)]
    return mtrRetur

def somar(m1, m2):
    matriz_soma = []

    quant_linhas = len(m1)  # Conta quantas linhas existem na primeira Matriz
    quant_colunas = len(m1[0])
    quant_linhas2 = len(m2) # Conta quantas linhas existem na seguna Matriz
    quant_colunas2 = len(m2[0]) # Conta quantos elementos têm em uma linha

    if  (quant_colunas != quant_colunas2) or (quant_linhas != quant_linhas2):
        return None
    else:
        for i in range(quant_linhas):
            # Cria uma nova linha na matriz_soma
            matriz_soma.append([])
            for j in range(quant_colunas):
                # Somando os elementos que possuem o mesmo índice
                soma = m1[i][j] + m2[i][j]
                matriz_soma[i].append(soma)
        return matriz_soma

def multiplicar(m1, m2):
    matriz_soma = []

    quant_linhas = len(m1)  # Conta quantas linhas existem na primeira Matriz
    quant_colunas = len(m1[0])
    quant_linhas2 = len(m2) # Conta quantas linhas existem na seguna Matriz

    if  quant_colunas != quant_linhas2:
        return None
    else:
        for i in range(quant_linhas):
            # Cria uma nova linha na matriz_soma
            matriz_soma.append([])
            for j in range(quant_colunas):
                # Somando os elementos que possuem o mesmo índice
                mult = m1[i][j] * m2[j][i]
                matriz_soma[i].append(mult)
        return matriz_soma


arrayTest = gerarMatriz(mtr1Li,mtr1Col, minimo, maximo)
arrayTest2 = gerarMatriz(mtr2Li,mtr2Col, minimo, maximo)

for item in arrayTest:

    print(str(item).replace("[","").replace(",","").replace("]",""))

print(" ")
print(" ")

for item in arrayTest2:
    print(str(item).replace("[","").replace(",","").replace("]",""))

print(" ")
print(" ")

matrizSum = somar(arrayTest, arrayTest2)

if matrizSum == None:
    print("Não é possível somar matrizes de dimensões diferentes")
else:
    for item in matrizSum:
        print(str(item).replace("[", "").replace(",", "").replace("]", ""))

print(" ")
print(" ")

matrizMulti = multiplicar(arrayTest, arrayTest2)

if matrizMulti == None:
    print("Não é possível multiplicar matrizes se a quantidade de colunas da primeira é diferente da quantidade de linhas da segunda")
else:
    for item in matrizMulti:
        print(str(item).replace("[", "").replace(",", "").replace("]", ""))
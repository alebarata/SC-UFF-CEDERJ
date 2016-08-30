# paes com mais de 100g not
# max tipo diferente de alimentos
# um alimento de cada tipo
casosTeste = 0

qtdAlm = 0
tiposDiferentes = 0

count = 1

alimentos = dict()
contadorGramas = 0

with open("Entradas/Q3input.txt", "r") as entrd:
    temp_line = entrd.readlines()
    casosTeste = int(temp_line[0])

    del temp_line[0]


    for i in range(casosTeste):
        temp_line2 = temp_line[0].split(' ', 1)
        qtdAlm = int(temp_line2[0])
        tiposDiferentes = int(temp_line2[1])
        if tiposDiferentes > 1:
            for e in range(0,qtdAlm+1):
                if count == 1:
                    count += 1
                else:
                    almTy = str(temp_line[e].split(' ')[0])
                    if almTy not in alimentos.keys():
                        alimentos.update({almTy:0})
                    almPes = int(temp_line[e].split(' ')[1])
                    if almPes < 100 and almPes > alimentos[almTy]:
                        alimentos.update({almTy:almPes})
            print(str(sum(alimentos.values())))
        else:
            print(int(temp_line[1].split(' ')[1]))

        count = 0
        alimentos = dict()
        del  temp_line[0:qtdAlm+1]

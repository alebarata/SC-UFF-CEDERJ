import  random

minimo = int(input('Informe o valor minimo da faixa: '))
maximo = int(input('Informe o valor maximo da faixa: '))
qtdElem = int(input('Informe a quantidade de elementos: '))

def preenchimentoRadomico(mi, max, elementos):
    myVet = []
    for i in range(elementos):
        myVet.append(random.randrange(mi,max))
    return  myVet

def removeDuplicates(vet):
    return list(set(vet))

def minMaxVal(vetor):
    vetRet = []
    mi = min(vetor)
    mai = max(vetor)
    minCount = 0
    maxCount = 0

    for item in vetor:
        if item == mi:
            minCount += 1
        elif item == mai:
            maxCount += 1

    vectorUnrepeated = list(set(vetor))
    if mi in vectorUnrepeated and minCount >=2:
        vectorUnrepeated.remove(mi)

    if mai in vectorUnrepeated and maxCount >=2:
        vectorUnrepeated.remove(mai)

    if not vectorUnrepeated:
        vetRet.append(None); vetRet.append(None)
    else:
        menor  = min(vectorUnrepeated)
        maior = max(vectorUnrepeated)

        if (menor != None or maior != None) and (menor != maior):
            vetRet.append(menor); vetRet.append(maior)

        if menor == maior:
            vetRet.append(menor)
            vetRet.append(maior)
    return vetRet


arrayTest = preenchimentoRadomico(minimo,maximo,qtdElem)

print(str(arrayTest), end='\n')

print(str(minMaxVal(arrayTest)))



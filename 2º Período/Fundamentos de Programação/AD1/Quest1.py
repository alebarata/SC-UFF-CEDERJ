
def decimalToAny(n, base):
    a = 0
    i = 0
    while n != 0:
        remainder = n % base
        n //= base

        if remainder < 0:
            remainder += abs(base)
            n += 1

        a += remainder * (10 ** i)
        i += 1
    return a

def converte(numeroDecimal):
    numConvertido = ''
    numDecimal = int(numeroDecimal)
    for i in range(2,10):
        if i == 2:
            numConvertido += '%s ' % (str(bin(numDecimal)[2:]))
        else:
            numConvertido += '%s ' % (str(decimalToAny(numDecimal, i)))
    return numConvertido

with open("Entradas/Q1input.txt", "r") as entrd:
    temp_line = entrd.readlines()
    lines = [int(i) for i in temp_line]

for i in lines:
    if i != -1:
        tempRes = converte(i)
        print('%d                %s' % (i, tempRes))
    else:
        print('%d                ' % (i))

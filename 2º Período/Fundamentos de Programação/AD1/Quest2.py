lines = list()

with open("Entradas/Q2input.txt", "r") as entrd:
    temp_line = entrd.readlines()
    lines = [str(i).rstrip('\n') for i in temp_line]



for i in range(len(lines)):
    if lines[i] == 'fim':
        print(lines[i])
        break
    else:
        original = lines[i].replace(' ', '').lower()
        inversed = lines[i].replace(' ', '').lower()[::-1]
        if original == inversed:
            print("%s                          é palíndromo" % (lines[i]))
        elif original != inversed:
            print("%s                          não é palíndromo" % (lines[i]))


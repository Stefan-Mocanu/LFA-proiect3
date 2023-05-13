def separare(x):
    global neterm
    if len(x)==1 and x == 'λ':
        return tuple('λ'), 0
    cnt = 0
    curent = ""
    l = []
    for litera in x:
        if litera == 'λ':
            continue
        if litera in neterm:
            if curent:
                l.append(curent)
            l.append(litera)
            curent = ""
        else:
            cnt += 1
            curent = curent + litera
    if curent:
        l.append(curent)
    return tuple(l), cnt


def genereaza(cuvinte,n):
    global prods
    global neterm
    #print(cuvinte)
    cuvs = []
    ok1 = True
    for elem1 in cuvinte:
        ok = True
        for ii, sec in enumerate(elem1[0]):
            if sec in neterm:
                ok = False
                ok1 = False
                for prod in prods[sec]:
                    if prod[0] == ['λ']:
                        a = "".join(elem1[0][:ii])
                        b = "".join(elem1[0][ii + 1:])
                        adaug = separare("".join((a, b)))
                        if adaug not in cuvs:
                            cuvs.append(adaug)
                        continue
                    if prod[1]+elem1[1] <= n:
                        a = "".join(elem1[0][:ii])
                        b = "".join(elem1[0][ii+1:])
                        c = "".join(prod[0])
                        adaug = separare("".join((a, c, b)))
                        if adaug not in cuvs:
                            cuvs.append(adaug)
        if ok and len(elem1[0][0]) == n:
            cuvs.append(elem1)
    if ok1:
        return cuvs
    return genereaza(cuvs, n)



f = open("input.in")
neterm = f.readline().split()
start = f.readline().strip()
prods = {x: [] for x in neterm}
aux = f.readline().split()
while aux:
    prods[aux[0]] = [separare(x) for x in aux[1:]]
    for i, el in enumerate(prods[aux[0]]):
        if 'lb' in el[0]:
            prods[aux[0]][i] = (('λ',), 0)
    aux = f.readline().split()

n = int(input("Ce lungime să aibă cuvintele generate: "))

cuvinte = [(tuple(start), 0)]

cuvinte = genereaza(cuvinte, n)
print(f"S-au generat {len(cuvinte)} cuvinte!")
for elem in cuvinte:
    print(elem[0][0])

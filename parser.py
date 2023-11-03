rules = ["S-aSb","S-c"]
nt = ["S"]
string = "a$"
c = 0
a = string[0]
flag = False
devolver = False
k = 0

def productions(N):
    productions = []
    for i in range(0, len(rules)):
        if rules[i][0] == N:
            productions.append((rules[i].split("-"))[1])
    return productions

def recursive_parser(N):
    global c
    global string
    global a 
    global k 
    flag = False
    global devolver
    listo = False

    parts = productions(N)
    for i in range(0, len(parts)):
        print(f'Estoy en la iteracion {i}')
        A = parts[i]
        print(f'La produccion es {A}')
        for j in range(0, len(A)):
            print(A[j])
            if A[j] in nt:
                print(f'{A[j]} es un no terminal')
                recursive_parser(A[j])
            elif A[j] == a:
                print(f'{A[j]} es igual let a = {a} ')
                c = c + 1
                a = string[c]
                k = k + 1
                flag = True
                if j == len(A) - 1:
                    print("piki")
                    listo = True
                    break
            else:
                print(f'{A[j]} no era la regla de produccion')
                if devolver == True:
                    print("Hice un break")
                    devolver = False
                break
        if listo == True:
            break
    if flag == False and devolver == False:
        print("Hola")
        c = c - 1
        a = string[c]
        k = k - 1
        devolver = True
    
recursive_parser("S")
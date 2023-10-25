rules = ["S-aSb", "S-c"]
nt = ["S"]
string = "aacbb"
c = 0
a = string[c]
flag = True


def set_parts(N):
    right = []
    for i in range(0, len(rules)):
        if rules[i][0] == N:
            right.append((rules[i].split("-"))[1])
    return right

def recursive_parser(N):
    global a 
    global c
    global flag
    it = 0

    parts = set_parts(N)
    
    if flag == True:
        A = parts[it]
    else:
        it = it + 1
        A = parts[it]
        print(A)

    for i in range(0, len(A) - 1):
        print(f'Iteracion {i}')
        if A[i] in nt:
            print("Es un no terminal")
            print(f'Xi = {A[i]}')
            recursive_parser(A[i])
        elif A[i] == a:
            print("Coincide:")
            print(f'let a = {a}')
            c = c + 1
            a = string[c]
            print(f'Nuevo {a}')
            flag = True
        else:
            print("No es la regla de produccion")
            flag = False

recursive_parser("S")




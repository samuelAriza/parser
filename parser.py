rules = ["S-aSb", "S-c"]
nt = ["S"]
string = "acb"
c = 0
a = string[c]
flag = True


def set_parts(N):
    right = []
    for i in range(0, len(rules)):
        if rules[i][0] == N:
            right.append((rules[i].split("-"))[1])
    return right

it = 0

def validation(flag, N):
    global c
    global a
    global it

    parts = set_parts(N)
    if flag == True:
        A = parts[it]
        return A
    elif flag == False:
        if it >= len(parts) - 1:
            c = c - 1
            a = string[c]
        else:
            it = it + 1
            A = parts[it]
            return A

def recursive_parser(N):
    global a 
    global c
    global flag
    
    A = validation(flag, N)
    print(f'Ahora la regla es {A}')
    print(f'Let aaaa = {a}')
    print(f'El {A == None}')
    if A == None:
        return "no"

    for i in range(0, len(A)):
        print(f'Iteracion {i}')
        if A[i] in nt:
            print("Es un no terminal")
            print(f'Xi = {A[i]}')
            recursive_parser(A[i])
        elif A[i] == a:
            print("Coincide:")
            print(f'let a = {a}')
            c = c + 1
            try:
                a = string[c]
            except:
                return "yes"
            print(f'Nuevo {a}')
            flag = True
        else:
            print("No es la regla de produccion")
            flag = False
            recursive_parser(N)
            break

x = recursive_parser("S")
if x == "yes":
    print("yes")
elif x == None:
    print("no")
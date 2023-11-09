import re

rules = ["S-AB", "A-aA", "A-a", "B-bB", "B-b"]
nt = ["S", "A", "B"]

string = "aab"
S = string
count = 0
back = False
flag = False
recursion_num = 0
is_remaining = 0
remaining = False
bandera = False
aceptancia = False

def parts_of(N):
    parts = []
    for i in range(0, len(rules)):
        if rules[i][0] == N:
            parts.append((rules[i].split("-"))[1])
    return parts

def recursive_parser(N):
    global string
    global recursion_num
    global flag
    global count
    global back
    global S
    global is_remaining
    global bandera
    global aceptancia
    remaining = False


    parts = parts_of(N)


    for i in range(0, len(parts)):

        if flag == True:
            print("Hola")
            break

        print("-------")
        print(S)
        print(f'Regla {i}')
        A = parts[i]
        print(A)
        for j in range(0, len(A)):
            print("JAS")
            print(remaining)

            if remaining == True and back == True and is_remaining != 0 or is_remaining != 0 and flag == True and remaining == True and back == False:
                is_remaining = is_remaining - 1
                print(f'Actualizado {is_remaining}')
            
            if (A[j] in nt):
                print(f'{A[j]} es un no terminal')
                flag = False
                back = False
                
                temporal = A[j + 1:len(A)]

                if len(A) - 1 > j:
                    non_terminals = len(re.sub('[^A-Z]', '', temporal))
                    if non_terminals > 0:
                        is_remaining = is_remaining + non_terminals
                        bandera = True
                        print("ENTREEE")

                    is_remaining = is_remaining + (len(re.sub('[^a-z]', '', temporal)))
                    remaining = True
                    print(f'Queda en {is_remaining}')


                recursive_parser(A[j])

            elif (A[j] == S[0]):
                print("JUIKI")
                print(f'{S[0]} = {A[j]}')
                count = count + 1
                S = string[count:len(string)]
                flag = True  
                print(len(A) - 1)
                print(j) 
                print(is_remaining)
                print(len(S))
                print(bandera)
                print(f'Pero bueno {S}')
                if len(A) - 1 == j and is_remaining != len(S) and len(S) != 0 and bandera == False:
                    print("LOLO")
                    count = count - 1
                    S = string[count:len(string)]
                    print(f'{A} no era la regla de produccion')
                    flag = False
                    if back == True:
                        print("break")
                        back = False
                    break 
            else:
                print(f'{A} no era la regla de produccion')

                if flag == True:
                    count = count - 1
                    S = string[count:len(string)]

                flag = False

                if back == True:
                    print("break")
                    back = False
                break

        print("El pepe")

    if flag == False and back == False:
        print("lala")
        print(remaining)
        count = count - 1
        S = string[count:len(string)]
        back = True
    
    print("---")
    print(flag)
    print(remaining)
    print(back)
    print(is_remaining)
    print("---")

respuestas = []

try:
    print("SSS")
    recursive_parser("S")
except:
    string = string + "$"
    S = string
    count = 0
    back = False
    flag = False
    recursion_num = 0
    is_remaining = 0
    remaining = False
    bandera = False
    aceptancia = False
    recursive_parser("S")

if flag == True and len(S) == 0 or S[0] == "$":
    respuestas.append("yes")
else:
    respuestas.append("no") 

print(respuestas)
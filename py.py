for i in range(0, len(strings)):
    string = strings[i]
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
    print(flag)
    print(len(S))
    print(S)
    if flag == True and len(S) == 0 or S[0] == "$":
        respuestas.append("yes")
    else:
        respuestas.append("no")

print(respuestas)
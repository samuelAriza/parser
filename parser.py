import re

# Leer las dimensiones y datos de entrada
n, m, k = map(int, input().split())  # Lee tres números separados por espacios
nt = input().split()  # Lee una lista de no terminales (strings)
rules = [input() for _ in range(m)]  # Lee 'm' reglas de producción (strings)
strings = [input() for _ in range(k)]  # Lee 'k' cadenas a analizar (strings)

# Función para restablecer las variables globales antes de analizar una nueva cadena
def reset_globals():
    global S  # Cadena actual a analizar
    global count  # Índice de posición en la cadena
    global back  # Bandera para indicar si se debe retroceder en la cadena
    global flag  # Bandera para indicar el éxito del análisis
    global recursion_num  # Número de recursiones realizadas
    global is_remaining  # Cantidad de elementos por analizar en la cadena
    global remaining  # Bandera para indicar si quedan elementos por analizar en la cadena
    global bandera  # Bandera para varios fines internos
    global aceptancia  # Bandera para indicar la aceptación
    S = string
    count = 0
    back = False
    flag = False
    recursion_num = 0
    is_remaining = 0
    remaining = False
    bandera = False
    aceptancia = False

# Función para identificar las partes de la regla
def parts_of(N):
    parts = []  # Almacena las partes de la regla
    last = []  # Almacena las últimas partes de la regla
    for i in range(0, len(rules)):
        if rules[i][0] == N:
            x = ((rules[i].split("-"))[1])
            if x[0] != N:
                parts.append(x)
            else:
                last.append(x)

    # Ordenar las partes por longitud en orden descendente
    order_array_1 = sorted(parts, key=order_by_len, reverse=True)
    order_array_2 = sorted(last, key=order_by_len, reverse=True)

    result = order_array_1 + order_array_2
    return result

# Función para ordenar elementos por longitud
def order_by_len(element):
    return len(element)

# Función recursiva para analizar la cadena
def recursive_parser(N):
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
            break

        A = parts[i]

        for j in range(0, len(A)):
            if remaining == True and back == True and is_remaining != 0 or is_remaining != 0 and flag == True and remaining == True and back == False:
                is_remaining = is_remaining - 1

            if (A[j] in nt):
                flag = False
                back = False

                temporal = A[j + 1:len(A)]

                if len(A) - 1 > j:
                    non_terminals = len(re.sub('[^A-Z]', '', temporal))
                    if non_terminals > 0:
                        is_remaining = is_remaining + non_terminals
                        bandera = True

                    is_remaining = is_remaining + (len(re.sub('[^a-z]', '', temporal)))
                    remaining = True

                recursive_parser(A[j])

            elif (A[j] == S[0]):
                count = count + 1
                S = string[count:len(string)]
                flag = True

                if len(A) - 1 == j and is_remaining != len(S) and len(S) != 0 and bandera == False:
                    count = count - 1
                    S = string[count:len(string)]
                    flag = False
                    if back == True:
                        back = False
                    break
            else:
                if flag == True:
                    count = count - 1
                    S = string[count:len(string)]

                flag = False

                if back == True:
                    back = False
                break

    if flag == False and back == False:
        count = count - 1
        S = string[count:len(string)]
        back = True

respuestas = []

# Procesar cada cadena de entrada
for i in range(0, len(strings)):
    string = strings[i]
    reset_globals()
    try:
        recursive_parser("S")
    except:
        string = strings[i] + "$"
        S = string
        reset_globals()
        recursive_parser("S")

    if flag == True and len(S) == 0 or S[0] == "$":
        respuestas.append("yes")
    else:
        respuestas.append("no")

# Imprimir las respuestas
for response in respuestas:
    print(response)

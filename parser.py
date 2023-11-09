import re

n, m, k = map(int, input().split())
nt = input().split()
rules = [input() for _ in range(m)]
strings = [input() for _ in range(k)]

def reset_globals():
    global S
    global count
    global back
    global flag
    global recursion_num
    global is_remaining
    global remaining
    global bandera
    global aceptancia
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
    last = []
    for i in range(0, len(rules)):
        if rules[i][0] == N:
            x = ((rules[i].split("-"))[1])
            if x[0] != N:
                parts.append(x)
            else:
                last.append(x)

    order_array_1 = sorted(parts, key=order_by_len, reverse=True)
    order_array_2 = sorted(last, key=order_by_len, reverse=True)

    result = order_array_1 + order_array_2
    return result

def order_by_len(element):
    return len(element)

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

for response in respuestas:
    print(response)

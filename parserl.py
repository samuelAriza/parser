import re 

texto = "Texto Con Mayusculas y minusculas y num2344"


textoSoloMayusculas = re.sub('[^A-Z]', '', texto)

print("Mayusculas: " + str(len(textoSoloMayusculas)))
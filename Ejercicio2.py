# Hacer que el sistema genere un número aleatorio entre 1 y 10. 
# Luego hacer que el susario adivine el número. 
# La aplicación debe terminar cuando el usuario adivine.

import random
s = random.randint(1,10)

while True:
    n = int(input("Adivina el número del sistema:"))

    if n==s:
        print("Adivinaste")
        break
    else:
        print("Número incorrecto!")

        
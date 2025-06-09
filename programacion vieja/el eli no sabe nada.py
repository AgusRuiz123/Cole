"""
x = int(input("queres ingresar al menu 1 si 0 no"))

while x != 0:
    x = int(input("Hola ingresa 0 para salir"))

    print("vale x esto: ",x)

"""
"""

a = 0

for i in range(0,3):
    a = a + 1
    print("a vale: ",a)
    
"""
"""

pri = int(input("Cuantos años tiene el primer hermano: "))
seg = int(input("Cuantos años tiene el segundo hermano: "))

if pri == seg:
    print("Tienen la misma edad")

elif pri > seg:
    print("el primero es mayor")

elif pri < seg:
    print("el segundo es mayor")



a = 3
real_contra = 2429

q = int(input("Cuantos intentos queres: "))

for i in range(q):
    
    usu_contra = int(input("Ingresa la contraseña tenes 3 intentos: "))
    a = a - 1

    if usu_contra == real_contra:
        print("adivinaste la contraseña")
        break

    elif usu_contra != real_contra:
        print("intentalos de nuevo te quedan", a, "intentos")

"""
"""

n = 1


if n%2 == 0:
    print("pis")

elif n%2 != 0:
    print("caca")

"""




































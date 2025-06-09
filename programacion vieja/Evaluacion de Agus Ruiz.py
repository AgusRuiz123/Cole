lista = []

x = 1

while x != 0:

    menu = int(input("ingresa 0 para salir, 1 para ingresar algo a una lista y 2 para inmprimir Hola Mundo: "))

    if menu == 0:
        x = 0

    elif menu == 1:
        ingresar = input("Que quiere ingresar a la lista: ")
        lista.append(ingresar)
        print("La lista contiene", len(ingresar), "elemento que son los siguientes", lista)

    elif menu == 2:
        print("Hola Mundo")
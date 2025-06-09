f1 = ["ferrari", "mclaren", "aston martin", "mercedes", "red bull", "alpine", "kick", "haas", "williams", "rb"]
precios = [110000, 125000, 60000, 100000, 130000, 80000, 70000, 70000, 95000, 80000]
carrito = []
costo = int(0)

q = 1

while q != 0:

    menu = int(input("pone 0 para salir, 1 para agregar, 2 para borrar, 3 para buscar o 4 para comprar: "))

    if menu == 0:
        q = 0
        print("Finalizaste el programa manualmente. ")
    
    elif menu == 1:
            
        agregar = input("Ingrese el F1 que decea agregar: ")
        precio_agregar = input("Ingrese el precio de el F1 nuevo: ")

        f1.append(agregar)
        precios.append(precio_agregar)


    elif menu == 2:
        borrar = input("Ingrese el f1 que desea borrar: ")
        if borrar in f1:
            m = f1.index(borrar)
            del f1[m]
            del precios[m]
        else:
            print("El F1", borrar, "no existe")

    elif menu == 3:
        buscar = input("Ingrese el f1 que busca: ")
        if buscar in f1:
            m = f1.index(buscar)
            print("Un", buscar, "cuesta:", precios[m])
        else:
            print("El F1", buscar, "no existe")

    
    elif menu == 4:
        while menu == 4:
            print("La funcion de comprar contiene un carrito que usted le va a ingresar productos que quiera comprar")

            menu2 = int(input("Pone 0 si no queres hacer nada con el carrito, 1 para agregar al carrito, 2 para borrar y 3 para imprimir el carrito"))

            if menu2 == 0:
                menu = 10
            
            elif menu2 == 1:

                agregar_carrito = input("Que F1 quiere comprar: ")
                if agregar_carrito in f1:
                    carrito.append(agregar_carrito)
                    costo = costo + precios.index(f1.index(agregar_carrito))
        
                else:
                    print("El F1", agregar_carrito, "no existe")
            
            elif menu2 == 2:
                borrar_carrito = int(input("Ingrese el F1 que desea borrar: "))
                if borrar_carrito in carrito:

                    o = f1.index(borrar_carrito)
                    del carrito[o]

                    costo = costo - precios[o]

                else:
                    print("El F1", borrar_carrito, "no existe")
            
            elif menu2 == 3:
                for r in range(carrito()):

                    print("Un", carrito[r], "cuesta:", precios[carrito.index(r)])

    

    else:
        print("Error intentalo de nuevo")
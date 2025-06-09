f1 = ["ferrari", "mclaren", "aston martin", "mercedes", "red bull", "alpine", "kick", "haas", "williams", "rb"]
precios = [110000, 125000, 60000, 100000, 130000, 80000, 70000, 70000, 95000, 80000]

x = input("Que F1 decea comprar: ").lower

if x in f1:
    i = f1.index(x)
    print("Un", x, "cuesta:", precios[i])

else:
    print(x, "no se encuentra en la lista de F1")

hola = int(4)
while hola == 4:
    menu = input("Precione 0 para salir, 1 para agregar, 2 borrar, 3 buscar")

    if menu == 0:
        break

    elif menu == 3:
        

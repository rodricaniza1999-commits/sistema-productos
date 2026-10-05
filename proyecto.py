productos = []

while True:
    print("\033[32m" + "="*40 + "\033[0m")
    print("\033[32mSistema de gestion de productos\033[0m")
    print("\033[32m" + "="*40 + "\033[0m")
    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Encontrar productos")
    print("4. Quitar productos")
    print("5. Salir")

    opcion = input("Elegi una opción (1-5): ").strip()

    if opcion == "1":
        print("\033[32m--- Agregar producto ---\033[0m")

        nombre = input("Nombre del producto: ").strip()
        while nombre == "":
            print("Error: el nombre no puede estar vacio.")
            nombre = input("Nombre del producto: ").strip()

        categoria = input("Categoria del producto: ").strip()
        while categoria == "":
            print("Error: la categoria no puede estar vacia.")
            categoria = input("Categoria del producto: ").strip()

        precio_str = input("Precio (sin centavos): ").strip()
        while not precio_str.isdigit():
            print("Error: ingresa solo numeros positivos.")
            precio_str = input("Precio (sin centavos): ").strip()
        precio = int(precio_str)

        datos = [nombre, categoria, precio]
        productos.append(datos)
        print("¡Producto agregado con éxito!")

    elif opcion == "2":
        print("\033[32m--- Lista de productos ---\033[0m")

        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
        else:
            for i in range(len(productos)):
                print(f"ID:{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}")

    elif opcion == "3":
        print("\033[32m--- Buscar producto ---\033[0m")

        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
        else:
            busqueda = input("Nombre del producto a buscar: ").strip().lower()

            while busqueda == "":
                print("Error: escribi algo para buscar")
                busqueda = input("Nombre del producto a buscar: ").strip().lower()

            encontrado = 0
            for i in range(len(productos)):
                if busqueda in productos[i][0].lower():
                    print(f"ID:{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}")
                    encontrado += 1

            if encontrado == 0:
                print("No se encontro ningun resultado.")
            else:
                print(f"Productos encontrados: {encontrado}")

    elif opcion == "4":
        print("\033[32m--- Eliminar producto ---\033[0m")
        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
        else:
            for i in range(len(productos)):
                print(f"{i+1}. {productos[i][0]} - {productos[i][1]} (${productos[i][2]})")

            id_eliminar = input("Numero de producto a eliminar: ").strip()

            while not id_eliminar.isdigit() or int(id_eliminar) < 1 or int(id_eliminar) > len(productos):
                print("Error: ingresa un numero valido de la lista.")
                id_eliminar = input("Numero de producto a eliminar: ").strip()
                
            posicion = int(id_eliminar) - 1
            eliminado = productos.pop(posicion)
            print(f"Se elimino el producto: {eliminado[0]}")

    elif opcion == "5":
        print("\033[32m¡Gracias por usar nuestro sistema!\033[0m")
        break

    else:
        print("Opcion no valida. Tenes que elegir entre (1-5)")
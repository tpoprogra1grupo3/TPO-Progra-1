import os

def biblioteca():              # Crea un inventario incial
    libros = [
    ['Cien años de soledad', 'L001', 'Gabriel García Márquez', 5, 'Sudamericana', 25000],
    ['El principito', 'L002', 'Antoine de Saint-Exupéry', 10, 'Emecé', 13000],
    ['Don Quijote de la Mancha', 'L003', 'Miguel de Cervantes', 3, 'Alfaguara', 35000],
    ['1984', 'L004', 'George Orwell', 7, 'Destino', 18000],
    ['Orgullo y prejuicio', 'L005', 'Jane Austen', 6, 'Alianza', 7000],
    ['El señor de los anillos', 'L006', 'J.R.R. Tolkien', 2, 'Minotauro', 42000],
    ['Harry Potter y la piedra filosofal', 'L007', 'J.K. Rowling', 9, 'Salamandra', 28000],
    ['Matar un ruiseñor', 'L008', 'Harper Lee', 4, 'Debolsillo', 16000],
    ['Crónica de una muerte anunciada', 'L009', 'Gabriel García Márquez', 8, 'Norma', 8500],
    ['El código Da Vinci', 'L010', 'Dan Brown', 1, 'Planeta', 19500]
]
    return libros

def limpiar_consola(): # Vacía la consola
    os.system("cls")

def imprimir_libros(libros):     ##ESTA FUNCION MUESTRA LOS LIBROS COMO MATRIZ
    limpiar_consola()
    print(f"|{"Catálogo de Libros":-^60}|", end="\n\n")
    for libro in libros:
        print(f"Nombre: {libro[0]}")
        print(f"Código: {libro[1]}")
        print(f"Autor: {libro[2]}")
        print(f"Stock: {libro[3]}")
        print(f"Editorial: {libro[4]}")
        print(f"Precio: ${libro[5]:,.2f}")  # Muestra el precio con separadores
        print("-" * 20)         ##Separación entre los libros mostrados
    print("--- Fin del Catálogo ---")
    input("\nPresiona Enter para continuar...")

def añadir_libro(libros):        # VER TEMA ID DEL LIBRO Y COMO GENERAR!!!!!!!!!!
    limpiar_consola()
    print(f"|{"Bienvenido a la carga de libros":-^60}|", end="\n\n")
    nuevo_nombre_libro=input("Ingrese el nombre del nuevo libro: ").lower()
    nuevo_autor_libro=input("Ingrese el autor: ").lower()
    nuevo_editorial_libro=input("Ingrese la editorial del libro: ").lower()
    
    existente=False           ##Interruptor para saber si el libro ingresado ya existe

    for libro in libros:
        if (libro[0].lower()==nuevo_nombre_libro and
            libro[2].lower()==nuevo_autor_libro and     ##Compara todos los datos de los libros en minus con el ingresado
            libro[4].lower()==nuevo_editorial_libro):
            libro[3]+=1                                 ##Añade un ejemplar mas si el libro ya existe
            print(f"El libro {nuevo_nombre_libro} ya existe y se añadió un ejemplar más!!")
            existente=True
            return      ##Debe devolver algo por conveniencia para no seguir ejecutando codigo de la funcion

    if not existente:
        while True:
            nuevo_codigo_libro = input("Ingrese el nuevo código del libro (solo letras y números): ")
            if nuevo_codigo_libro.isalnum():
                break
            else:
                print("Código inválido. El código solo debe contener letras y números. Intente de nuevo.")

        while True:
            nuevo_precio = input("Ingrese el precio del libro (solo números): ")
            if nuevo_precio.isdigit():       ##Revisa que el precio sean solo números.
                nuevo_precio = float(nuevo_precio)
                break
            else:
                print("Precio inválido. Debe ser un número entero. Intente de nuevo.")

        nuevo_libro = [
            nuevo_nombre_libro.title(),
            nuevo_codigo_libro.title(),
            nuevo_autor_libro.title(),
            1,
            nuevo_editorial_libro.title(),
            nuevo_precio
        ]
        libros.append(nuevo_libro)
        print(f"\nEl libro '{nuevo_nombre_libro.title()}' se ha cargado con éxito en la biblioteca.")

def eliminar_libro(libros):     
    limpiar_consola()
    print(f"|{'Bienvenido a la eliminación de libros':-^60}|", end="\n\n")
    codigo_libro = input("Ingrese el nombre del libro a eliminar: ").lower()

    libro_encontrado = False
    for libro in libros:
        if libro[1].lower() == codigo_libro:
            libros.remove(libro)        ##Elimina el libro de la matriz
            print(f"El libro '{libro[0]}' se ha eliminado de la biblioteca.")
            libro_encontrado = True
            return
    
    if not libro_encontrado:
        print("No se encontró el libro especificado.")

def buscar_libro(libros):
    limpiar_consola()
    print(f"|{'Buscar libro en la biblioteca':-^60}|\n")
    print("¿Por qué criterio desea buscar el libro?")
    print("1. Nombre")
    print("2. Código")
    print("3. Autor")
    print("4. Stock")
    print("5. Editorial")
    print("6. Precio (por rango)")

    opcion = input("\nSeleccione una opción (1-6): ")

    campos = {
        "1": 0,  # Nombre
        "2": 1,  # Código
        "3": 2,  # Autor
        "4": 3,  # Stock
        "5": 4,  # Editorial
        "6": 5   # Precio
    }

    if opcion not in campos:
        print("Opción no válida.")
        input("\nPresiona Enter para continuar...")
        return

    indice = campos[opcion]
    resultados = []

    if opcion == "6":
        # Buscar por rango de precios
        while True:
            precio_min = input("Ingrese el precio mínimo: ")
            if precio_min.isdigit():
                precio_min = float(precio_min)
                break
            else:
                print("Ingrese un número válido.")

        while True:
            precio_max = input("Ingrese el precio máximo: ")
            if precio_max.isdigit():
                precio_max = float(precio_max)
                break
            else:
                print("Ingrese un número válido.")

        for libro in libros:
            precio = libro[5]
            if precio_min <= precio <= precio_max:
                resultados.append(libro)

    else:
        valor = input("Ingrese el valor a buscar: ").lower()

        for libro in libros:
            campo = str(libro[indice]).lower()

            if opcion in ["2", "4"]:  # Código y Stock: búsqueda exacta
                if campo == valor:
                    resultados.append(libro)
            else:  # Nombre, Autor, Editorial: búsqueda parcial del input solicitado
                if valor in campo:
                    resultados.append(libro)

    limpiar_consola()
    if resultados:
        print(f"\nSe encontraron {len(resultados)} libro(s):\n")
        for libro in resultados:
            print(f"Nombre: {libro[0]}")
            print(f"Código: {libro[1]}")
            print(f"Autor: {libro[2]}")
            print(f"Stock: {libro[3]}")
            print(f"Editorial: {libro[4]}")
            print(f"Precio: ${libro[5]:,.2f}")
            print("-" * 20)
    else:
        print("No se encontraron libros con ese criterio.")
    
    input("\nPresiona Enter para continuar...")




##El MAIN DEBE SER MODIFICADO PARA ADMINISTRADOR Y CLIENTE
##CUIDADO CON EL ACENTO EN LOS NOMBRES DE LOS LIBROS
##CREAR ROL EMPLEADO



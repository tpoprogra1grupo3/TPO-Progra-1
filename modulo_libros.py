import os
import re
from funciones_utiles import es_numero_flotante, convertir_a_flotante

def biblioteca():              # Crea un inventario incial
    libros = [
    ['Cien años de soledad', 'L001', 'Gabriel García Márquez', 5, 'Sudamericana', 25000.0],
    ['El principito', 'L002', 'Antoine de Saint-Exupéry', 10, 'Emecé', 13000.0],
    ['Don Quijote de la Mancha', 'L003', 'Miguel de Cervantes', 3, 'Alfaguara', 35000.0],
    ['1984', 'L004', 'George Orwell', 7, 'Destino', 18000.0],
    ['Orgullo y prejuicio', 'L005', 'Jane Austen', 6, 'Alianza', 7000.0],
    ['El señor de los anillos', 'L006', 'J.R.R. Tolkien', 2, 'Minotauro', 42000.0],
    ['Harry Potter y la piedra filosofal', 'L007', 'J.K. Rowling', 9, 'Salamandra', 28000.0],
    ['Matar un ruiseñor', 'L008', 'Harper Lee', 4, 'Debolsillo', 16000.0],
    ['Crónica de una muerte anunciada', 'L009', 'Gabriel García Márquez', 8, 'Norma', 8500.0],
    ['El código Da Vinci', 'L010', 'Dan Brown', 1, 'Planeta', 19500.0]
]
    return libros

def limpiar_consola(): # Vacía la consola
    os.system("cls")

def imprimir_libros(libros):
    limpiar_consola()
    print(f"|{'Catálogo de Libros':-^120}|\n")
    
    # Encabezado
    encabezado = f"{'Nombre':<35} {'Código':<8} {'Autor':<25} {'Stock':<7} {'Editorial':<20} {'Precio':>10}"
    print(encabezado)
    print("-" * 120)

    # Libros
    for libro in libros:
        nombre, codigo, autor, stock, editorial, precio = libro
        linea = f"{nombre:<35} {codigo:<8} {autor:<25} {stock:<7} {editorial:<20} ${precio:>9,.2f}"
        print(linea)

    print("-" * 120)

def añadir_libro(libros):        
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

    
    nuevo_codigo_libro = generar_id_libro(libros)
    print(nuevo_codigo_libro)

    while True:                                         # Caso de que el libro no exista (Es nuevo)
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
    """Elimina un libro por ID."""
    limpiar_consola()
    print(f"|{'Bienvenido a la eliminación de libros':-^60}|\n")
    id_libro = input("Ingrese el ID del libro a eliminar (ej: L001): ").upper()

    for libro in libros:
        if libro[1] == id_libro:
            libros.remove(libro)  # Elimina el libro de la lista
            print(f"\nEl libro '{libro[0]}' (ID: {libro[1]}) se ha eliminado de la biblioteca.")
            return

    print("\nNo se encontró ningún libro con ese ID.")

def buscar_libro(libros):
    limpiar_consola()
    print(f"|{'Buscar libro en la biblioteca':-^120}|\n")
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
            precio_min = input("Ingrese el precio mínimo (use ',' o '.' para decimales): ").strip()
            if es_numero_flotante(precio_min):
                precio_min = convertir_a_flotante(precio_min)
                break
            else:
                print("Error: Ingrese un número válido.")

        while True:
            precio_max = input("Ingrese el precio máximo (use ',' o '.' para decimales): ").strip()
            if es_numero_flotante(precio_max):
                precio_max = convertir_a_flotante(precio_max)
                break
            else:
                print("Error: Ingrese un número válido.")

        # Lambda para filtrar precios
        filtro = lambda libro: precio_min <= libro[5] <= precio_max

    else:
        valor = input("Ingrese el valor a buscar: ").strip()

        if opcion in ["2", "4"]:  # Código y Stock: comparación exacta
            filtro = lambda libro: str(libro[indice]).lower() == valor.lower()
        else:
            # Nombre, Autor, Editorial: coincidencia parcial (regex)
            patron = re.compile(re.escape(valor), re.IGNORECASE)
            filtro = lambda libro: bool(patron.search(str(libro[indice])))

    # Aplica el filtro
    resultados = list(filter(filtro, libros))

    limpiar_consola()
    if resultados:
        print(f"|{'Resultados de la búsqueda':-^120}|\n")

        # Encabezado
        encabezado = f"{'Nombre':<35} {'Código':<8} {'Autor':<25} {'Stock':<7} {'Editorial':<20} {'Precio':>10}"
        print(encabezado)
        print("-" * 120)

        for libro in resultados:
            nombre, codigo, autor, stock, editorial, precio = libro

            # Si el nombre o autor exceden su espacio, se corta:
            nombre = (nombre[:32] + '...') if len(nombre) > 35 else nombre
            autor = (autor[:22] + '...') if len(autor) > 25 else autor
            editorial = (editorial[:17] + '...') if len(editorial) > 20 else editorial

            linea = f"{nombre:<35} {codigo:<8} {autor:<25} {stock:<7} {editorial:<20} ${precio:>9,.2f}"
            print(linea)

        print("-" * 120)
    else:
        print("No se encontraron libros con ese criterio.")

def actualizar_libro(libros):
    limpiar_consola()
    print(f"|{'Actualizar datos de un libro':-^120}|\n")
    id_libro = input("Ingrese el ID del libro que desea actualizar (ej: L001): ").upper()

    # Busca el libro por ID
    libro_encontrado = None
    for libro in libros:
        if libro[1] == id_libro:
            libro_encontrado = libro
            break

    if not libro_encontrado:
        print("\nNo se encontró ningún libro con ese ID.")
        return

    # Muestra información actual del libro
    limpiar_consola()
    print(f"|{'Información actual del libro':-^120}|\n")
    
    encabezado = f"{'N°':<3} {'Campo':<15} {'Valor Actual':<60}"
    print(encabezado)
    print("-" * 120)

    print(f"{'1':<3} {'Nombre':<15} {libro_encontrado[0]:<60}")
    print(f"{'2':<3} {'Autor':<15} {libro_encontrado[2]:<60}")
    print(f"{'3':<3} {'Stock':<15} {libro_encontrado[3]:<60}")
    print(f"{'4':<3} {'Editorial':<15} {libro_encontrado[4]:<60}")
    print(f"{'5':<3} {'Precio':<15} ${libro_encontrado[5]:,.2f}")
    print("-" * 120)

    # Selecciona campo para actualizar
    opcion = input("\nSeleccione el número del campo que desea actualizar (1-5): ")

    if opcion == "1":
        nuevo_nombre = input("Ingrese el nuevo nombre del libro: ").title()
        libro_encontrado[0] = nuevo_nombre
    elif opcion == "2":
        nuevo_autor = input("Ingrese el nuevo autor: ").title()
        libro_encontrado[2] = nuevo_autor
    elif opcion == "3":
        while True:
            nuevo_stock = input("Ingrese el nuevo stock (número entero): ")
            if nuevo_stock.isdigit():
                libro_encontrado[3] = int(nuevo_stock)
                break
            else:
                print("Stock inválido. Intente nuevamente.")
    elif opcion == "4":
        nueva_editorial = input("Ingrese la nueva editorial: ").title()
        libro_encontrado[4] = nueva_editorial
    elif opcion == "5":
        while True:
            nuevo_precio = input("Ingrese el nuevo precio (solo números o decimales '.'): ")
            if nuevo_precio.replace('.', '', 1).isdigit():
                libro_encontrado[5] = float(nuevo_precio)
                break
            else:
                print("Precio inválido. Intente nuevamente.")
    else:
        print("\nOpción no válida.")
        return

    print("\n¡El libro ha sido actualizado correctamente!")

def generar_id_libro(libros):
    """Genera un ID secuencial siguiendo el patron LXXX."""
    numeros_existentes = []
    for libro in libros:
        codigo = libro[1]
        if codigo.startswith('L') and codigo[1:].isdigit():
            numeros_existentes.append(int(codigo[1:]))
    
    if numeros_existentes:
        nuevo_numero = max(numeros_existentes) + 1
    else:
        nuevo_numero = 1

    return f"L{nuevo_numero:03d}"
            
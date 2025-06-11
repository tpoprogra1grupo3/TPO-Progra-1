import os
import re
from funciones_utiles import es_numero_flotante, convertir_a_flotante

def cargar_libros():
    try:    
        libros = []
        with open("Archivos_TXT/libros.txt", "r", encoding="UTF-8") as archivo_libros: 
            libros = biblioteca(archivo_libros,libros)
            return libros 
    except:
        print("Hubo un error al cargar los libros desde los archivos de programa")
        

def biblioteca(archivo_libros,libros):              # Carga la bibloteca desde el .txt
    libro_seleccionado = archivo_libros.readline().strip()
    if libro_seleccionado == "":
        return libros
    else:
        libro_seleccionado = list(libro_seleccionado.split(","))
        libro_seleccionado[3] = int(libro_seleccionado[3])
        libros.append(libro_seleccionado)
        return biblioteca(archivo_libros,libros)



def limpiar_consola(): # Vacía la consola
    os.system("cls")

def imprimir_libros(libros):
    limpiar_consola()
    print(f"|{'Catálogo de Libros':-^120}|\n")
    
    # Encabezado
    encabezado = f"{'Nombre':<35} {'Código':<8} {'Autor':<25} {'Stock':<7} {'Editorial':<20}"
    print(encabezado)
    print("-" * 120)

    # Libros
    for libro in libros:
        nombre, codigo, autor, stock, editorial= libro
        linea = f"{nombre:<35} {codigo:<8} {autor:<25} {stock:<7} {editorial:<20}"
        print(linea)

    print("-" * 120)

def añadir_libro(libros):
    limpiar_consola()
    print(f"|{'Bienvenido a la carga de libros':-^60}|", end="\n\n")
    nuevo_nombre_libro = input("Ingrese el nombre del nuevo libro (-1 para volver al menu de admin): ").lower()
    if nuevo_nombre_libro.strip() == "-1":
        return
    nuevo_autor_libro = input("Ingrese el autor (-1 para volver al menu de admin): ").lower()
    if nuevo_autor_libro.strip() == "-1":
        return
    nuevo_editorial_libro = input("Ingrese la editorial del libro (-1 para volver al menu de admin): ").lower()
    if nuevo_editorial_libro.strip() == "-1":
        return
    
    existente = False  # Interruptor para saber si el libro ingresado ya existe

    for libro in libros:
        if (libro[0].lower() == nuevo_nombre_libro and
            libro[2].lower() == nuevo_autor_libro and
            libro[4].lower() == nuevo_editorial_libro):
            libro[3] += 1  # Añade un ejemplar más si el libro ya existe
            print(f"El libro '{nuevo_nombre_libro.title()}' ya existe y se añadió un ejemplar más!!")
            existente = True
            return

    nuevo_codigo_libro = generar_id_libro(libros)

        
    nuevo_libro = [
        nuevo_nombre_libro.title(),
        nuevo_codigo_libro.title(),
        nuevo_autor_libro.title(),
        1,
        nuevo_editorial_libro.title(),
    ]
    libros.append(nuevo_libro)
    
    try:
        guardar_cambios_libros(libros)
        print(f"\nEl libro '{nuevo_nombre_libro.title()}' se ha cargado con éxito en la biblioteca.")
        return
    except:
        print("\n Ha ocurrido un Error al guardar los datos, contactar con soporte")
    

def eliminar_libro(libros):
    """Elimina un libro por ID."""
    limpiar_consola()
    print(f"|{'Bienvenido a la eliminación de libros':-^60}|\n")
    id_libro = input("Ingrese el ID del libro a eliminar (ej: L001)(-1 para volver): ").upper()
    if id_libro.strip() == "-1":
        return

    for libro in libros:
        if libro[1] == id_libro:
            libros.remove(libro)  # Elimina el libro de la lista
            try:
                guardar_cambios_libros(libros)
                print(f"\nEl libro '{libro[0]}' (ID: {libro[1]}) se ha eliminado de la biblioteca.")
                return
            except:
                print("\n Ha ocurrido un Error al guardar los datos, contactar con soporte")
    
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

    opcion = input("\nSeleccione una opción (1-6)(-1 para cancelar la búsqueda): ")
    if opcion.strip() == "-1":
        return
    
    campos = {
        "1": 0,  # Nombre
        "2": 1,  # Código
        "3": 2,  # Autor
        "4": 3,  # Stock
        "5": 4,  # Editorial
    }

    if opcion not in campos:
        print("Opción no válida.")
        input("\nPresiona Enter para continuar...")
        return

    indice = campos[opcion]     # indice es la fila de ese valor en la lista del libro 
    resultados = []


    valor = input("Ingrese el valor a buscar (-1 para cancelar): ").strip()
    if valor.strip() == "-1":
        return

    # Se Busca coinicidencias exactas y parciales
    if opcion in ["2", "4"]:  # Código y Stock: comparación exacta
        filtro = lambda libro: str(libro[indice]).lower() == valor.lower()
    else:
        # Nombre, Autor, Editorial: coincidencia parcial (regex)    
        patron = re.compile(re.escape(valor), re.IGNORECASE)        # "escape" ignora caracteres especiales
        filtro = lambda libro: bool(patron.search(str(libro[indice])))

    # Aplica el filtro
    resultados = list(filter(filtro, libros))

    limpiar_consola()
    if resultados:
        print(f"|{'Resultados de la búsqueda':-^120}|\n")

        # Encabezado
        encabezado = f"{'Nombre':<35} {'Código':<8} {'Autor':<25} {'Stock':<7} {'Editorial':<20}"
        print(encabezado)
        print("-" * 120)

        for libro in resultados:
            nombre, codigo, autor, stock, editorial= libro

            # Si el nombre o autor exceden su espacio, se corta:
            nombre = (nombre[:32] + '...') if len(nombre) > 35 else nombre
            autor = (autor[:22] + '...') if len(autor) > 25 else autor
            editorial = (editorial[:17] + '...') if len(editorial) > 20 else editorial

            linea = f"{nombre:<35} {codigo:<8} {autor:<25} {stock:<7} {editorial:<20}"
            print(linea)

        print("-" * 120)
    else:
        print("No se encontraron libros con ese criterio.")

def actualizar_libro(libros):
    limpiar_consola()
    print(f"|{'Actualizar datos de un libro':-^120}|\n")
    id_libro = input("Ingrese el ID del libro que desea actualizar (ej: L001)(-1 para cancelar): ").upper()
    if id_libro.strip() == "-1":
        return

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
    
    encabezado = f"{'N°':<3} {'Campo':<15}"
    print(encabezado)
    print("-" * 120)

    print(f"{'1':<3} {'Nombre':<15} {libro_encontrado[0]:<60}")
    print(f"{'2':<3} {'Autor':<15} {libro_encontrado[2]:<60}")
    print(f"{'3':<3} {'Stock':<15} {libro_encontrado[3]:<60}")
    print(f"{'4':<3} {'Editorial':<15} {libro_encontrado[4]:<60}")
    print("-" * 120)

    # Selecciona campo para actualizar
    opcion = input("\nSeleccione el número del campo que desea actualizar (1-5)(-1 para cancelar): ")
    if opcion.strip() == "-1":
        return
    elif opcion == "1":
        nuevo_nombre = input("Ingrese el nuevo nombre del libro (-1 para cancelar): ").title()
        if nuevo_nombre.strip() == "-1":
            return
        libro_encontrado[0] = nuevo_nombre
    elif opcion == "2":
        nuevo_autor = input("Ingrese el nuevo autor (-1 para cancelar): ").title()
        if nuevo_autor.strip() == "-1":
            return
        libro_encontrado[2] = nuevo_autor
    elif opcion == "3":
        while True:
            nuevo_stock = input("Ingrese el nuevo stock (número entero)(-1 para cancelar): ")
            if nuevo_stock.strip() == "-1":
                return
            if nuevo_stock.isdigit():
                libro_encontrado[3] = int(nuevo_stock)
                break
            else:
                print("Stock inválido. Intente nuevamente.")
    elif opcion == "4":
        nueva_editorial = input("Ingrese la nueva editorial (-1 para cancelar): ").title()
        if nueva_editorial.strip() == "-1":
            return
        libro_encontrado[4] = nueva_editorial
    else:
        print("\nOpción no válida.")
        return

    try:
        guardar_cambios_libros(libros)
        print("\n¡El libro ha sido actualizado correctamente!")
    except:
        print("\n Ha ocurrido un Error al guardar los datos, contactar con soporte")

def generar_id_libro(libros):    #Genera un ID secuencial siguiendo el patrón LXXX usando set.
    numeros_existentes = set()

    for libro in libros:
        codigo = libro[1]
        if codigo.startswith('L') and codigo[1:].isdigit():
            numeros_existentes.add(int(codigo[1:]))

    if numeros_existentes:
        nuevo_numero = max(numeros_existentes) + 1
    else:
        nuevo_numero = 1

    return f"L{nuevo_numero:03d}" 


def guardar_cambios_libros(libros):     # Reescribe los datos de libros
    filas_libros = [f"{nombre},{id_libro},{autor},{int(stock)},{editorial}\n" for nombre,id_libro,autor,stock,editorial in libros]
    try:
        with open("Archivos_TXT/libros.txt", "w", encoding="UTF-8") as archivo_libros: # Abre y cierra el archivo 
            try:
                archivo_libros.writelines(filas_libros)
            except:
                print("No se han podido guardar los cambios en los archivos de programa")
    except:
        print("No se ha podido abrir el archivo")

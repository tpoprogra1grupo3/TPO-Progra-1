from datetime import datetime, date, time, timedelta
from funciones_utiles import buscar_nombre_usuario, limpiar_consola
from modulo_libros import imprimir_libros

def crud_prestamos():
    prestamos = [
        ["Facu", 133185723, 'El principito', 'L002', "Antoine de Saint-Exupéry", 'Emecé', 1300, date.today(), (date.today() + timedelta(weeks=1)), "En curso"],
        ["Facu", 133185723, '1984', 'L004', "George Orwell", 'Destino', 5400, date.today(), (date.today() + timedelta(weeks=3)), "En curso"]
    ]
    return prestamos

def crear_prestamos(usuarios_datos, libros, prestamos):
    while True:
        libros_disponibles = [libro for libro in libros if libro[3] > 0]

        if not libros_disponibles:
            print("\nNo hay libros disponibles para préstamo.\n")
            return

        print("\n| Libros disponibles para préstamo |\n")
        print(f"{'N°':<4} {'Nombre':<35} {'Código':<8} {'Autor':<25} {'Stock':<7} {'Editorial':<20} {'Precio':>10}")
        print("-" * 125)

        for i, libro in enumerate(libros_disponibles, start=1):
            nombre, codigo, autor, stock, editorial, precio = libro
            print(f"{i:<4} {nombre:<35} {codigo:<8} {autor:<25} {stock:<7} {editorial:<20} ${precio:>9,.2f}")

        print("-" * 125)

        opcion_libro = input("\nIngrese el número del libro que desea alquilar (o '0' para cancelar): ").strip()
        if opcion_libro == "0":
            print("\nOperación cancelada.\n")
            return
        
        if not opcion_libro.isdigit() or not (1 <= int(opcion_libro) <= len(libros_disponibles)):
            print("\nNúmero inválido. Intente nuevamente.\n")
            continue

        indice_libro = int(opcion_libro) - 1
        libro_seleccionado = libros_disponibles[indice_libro]
        fila_libro = libros.index(libro_seleccionado)

        semanas_a_alquilar = input("\nIngrese la cantidad de semanas que desea alquilar el libro (o '0' para cancelar): ").strip()
        if semanas_a_alquilar == "0":
            print("\nOperación cancelada.\n")
            return

        if not semanas_a_alquilar.isdigit() or semanas_a_alquilar == "0":
            print("\nLa cantidad de semanas ingresada es inválida.\n")
            continue

        semanas_a_alquilar = int(semanas_a_alquilar)

        usuario_que_alquila = input("\nIngrese el nombre del usuario que desea alquilar el libro (o '0' para cancelar): ").strip()
        if usuario_que_alquila == "0":
            print("\nOperación cancelada.\n")
            return

        if not usuario_que_alquila.isalnum():
            print("\nEl nombre de usuario ingresado es inválido.\n")
            continue

        nombre_real = buscar_nombre_usuario(usuarios_datos, usuario_que_alquila)
        if nombre_real is None:
            print("\nEl usuario ingresado no existe.\n")
            continue

        id_usuario_que_alquila = usuarios_datos[nombre_real]['id']

        nombre_libro = libro_seleccionado[0]
        id_libro = libro_seleccionado[1]
        autor_libro = libro_seleccionado[2]
        editorial = libro_seleccionado[4]
        precio = (libro_seleccionado[5]) * (semanas_a_alquilar / 10)
        
        fecha_de_creacion = date.today()
        fecha_de_vencimiento = date.today() + timedelta(weeks=semanas_a_alquilar)

        print("\n\nLos datos del préstamo son: ")
        print(f"{nombre_real} | {id_usuario_que_alquila} | {nombre_libro} | {id_libro} | {autor_libro} | {editorial} | ${precio:.2f} | {estado_prestamo(fecha_de_vencimiento)}")
        print(f"\nFecha de inicio: {fecha_de_creacion}")
        print(f"Fecha de vencimiento: {fecha_de_vencimiento}\n")
        print("1. Confirmar los datos del préstamo")
        print("2. Cancelar el préstamo")

        opcion = input("Ingrese la opción que desea utilizar: ").strip()
        if opcion == "1":
            prestamo = [
                nombre_real,
                id_usuario_que_alquila,
                nombre_libro,
                id_libro,
                autor_libro,
                editorial,
                precio,
                fecha_de_creacion,
                fecha_de_vencimiento,
                estado_prestamo(fecha_de_vencimiento)
            ]
            prestamos.append(prestamo)
            libros[fila_libro][3] -= 1
            limpiar_consola()
            print("Se ha creado el préstamo exitosamente")
            return  # Sale al terminar
        elif opcion == "2":
            print("\nPréstamo cancelado.\n")
            return
        else:
            print("\nLa opción ingresada es inválida.\n")

def estado_prestamo(fecha_vencimiento):
    if fecha_vencimiento < date.today():
        return "Vencido"
    else:
        return "En curso"

def cambio_estado_inicio(prestamos):
    for fila in prestamos:
        fecha_vencimiento = fila[8]
        estado = estado_prestamo(fecha_vencimiento)
        fila[9] = estado

def imprimir_prestamos(prestamos, filtro="todos"):
    limpiar_consola()
    if not prestamos:
        print("| No hay préstamos registrados |")
        return
    
    print(f"|{'Listado de Préstamos':-^190}|")
    
    # Encabezado de tabla
    print(f"{'N°':<4}{'Usuario':<15}{'DNI':<12}{'Libro':<25}{'Código':<8}{'Autor':<25}{'Editorial':<15}{'Precio':<10}{'Inicio':<12}{'Vencimiento':<14}{'Estado':<10}")
    print("-" * 190)

    hoy = date.today()
    contador = 0

    for i, prestamo in enumerate(prestamos, 1):
        # Asegurar que cada campo tenga un valor válido para impresión
        usuario = prestamo[0] if prestamo[0] is not None else "Sin datos"
        dni = str(prestamo[1]) if prestamo[1] is not None else "Sin datos"
        libro = prestamo[2] if prestamo[2] is not None else "Sin datos"
        codigo = prestamo[3] if prestamo[3] is not None else "Sin datos"
        autor = prestamo[4] if prestamo[4] is not None else "Sin datos"
        editorial = prestamo[5] if prestamo[5] is not None else "Sin datos"
        precio = prestamo[6] if prestamo[6] is not None else 0.0

        fecha_inicio = prestamo[7].strftime('%d/%m/%Y') if isinstance(prestamo[7], date) else "Fecha inválida"
        fecha_vencimiento = prestamo[8].strftime('%d/%m/%Y') if isinstance(prestamo[8], date) else "Fecha inválida"
        estado_actual = estado_prestamo(prestamo[8]) if isinstance(prestamo[8], date) else "Desconocido"
        
        dias_restantes = (prestamo[8] - hoy).days if isinstance(prestamo[8], date) else 0

        color = "\033[0m"  # Color por defecto
        mostrar = True     # Bandera para filtrar

        if estado_actual == "Vencido":
            color = "\033[91m"  # Rojo
            if filtro == "en curso" or filtro == "por vencer":
                mostrar = False
        elif dias_restantes <= 3:
            color = "\033[93m"  # Amarillo
            if filtro == "vencido" or filtro == "en curso":
                mostrar = False
        else:
            color = "\033[92m"  # Verde
            if filtro == "vencido" or filtro == "por vencer":
                mostrar = False

        if filtro == "todos":
            mostrar = True

        if mostrar:
            contador += 1
            print(f"{contador:<4}{usuario:<15}{dni:<12}{libro:<25}{codigo:<8}{autor:<25}{editorial:<15}${precio:<9.2f}{fecha_inicio:<12}{fecha_vencimiento:<14}{color}{estado_actual:<10}\033[0m")

    if contador == 0:
        print("No se encontraron préstamos según el filtro aplicado.")
    
    print("-" * 190)

def ver_prestamos_con_filtro(prestamos):
    limpiar_consola()
    print(f"|{'Ver Préstamos':-^50}|")
    print("1. Ver todos los préstamos")
    print("2. Ver sólo préstamos en curso")
    print("3. Ver sólo préstamos vencidos")
    print("4. Ver préstamos próximos a vencer (3 días o menos)")
    print("9. Volver al menú anterior")
    
    opcion = input("\nSeleccione una opción:\n> ")

    if opcion == "1":
        imprimir_prestamos(prestamos, filtro="todos")
    elif opcion == "2":
        imprimir_prestamos(prestamos, filtro="en curso")
    elif opcion == "3":
        imprimir_prestamos(prestamos, filtro="vencido")
    elif opcion == "4":
        imprimir_prestamos(prestamos, filtro="por vencer")
    elif opcion == "9":
        return
    else:
        print("Opción inválida.")

def actualizar_prestamo(prestamos):
    limpiar_consola()
    if not prestamos:
        print("| No hay préstamos para actualizar |")
        return
    
    imprimir_prestamos(prestamos)

    nro = input("\nIngrese el número de préstamo que desea actualizar: ")
    if nro.isnumeric():
        nro = int(nro) - 1
        if 0 <= nro < len(prestamos):
            limpiar_consola()
            print("¿Qué desea actualizar del préstamo?")
            print("1. Estado (se recalcula automáticamente)")
            print("2. Fecha de vencimiento")
            opcion = input("Ingrese opción: ")

            if opcion == "1":
                fecha_vencimiento = prestamos[nro][8]
                prestamos[nro][9] = estado_prestamo(fecha_vencimiento)
                print("Estado recalculado correctamente.")
            elif opcion == "2":
                semanas_extra = input("Ingrese cuántas semanas desea extender el préstamo: ")
                if semanas_extra.isnumeric() and int(semanas_extra) > 0:
                    semanas_extra = int(semanas_extra)
                    prestamos[nro][8] = prestamos[nro][8] + timedelta(weeks=semanas_extra)
                    prestamos[nro][9] = estado_prestamo(prestamos[nro][8])
                    print("Fecha de vencimiento actualizada correctamente.")
                else:
                    print("Cantidad de semanas inválida.")
            else:
                print("Opción inválida.")
        else:
            print("Número de préstamo inválido.")
    else:
        print("Debe ingresar un número válido.")

def eliminar_prestamo(prestamos):
    limpiar_consola()
    if not prestamos:
        print("| No hay préstamos para eliminar |")
        return
    
    imprimir_prestamos(prestamos)

    nro = input("\nIngrese el número de préstamo que desea eliminar: ")
    if nro.isnumeric():
        nro = int(nro) - 1
        if 0 <= nro < len(prestamos):
            prestamo = prestamos[nro]
            confirmacion = input(f"\n¿Confirma eliminar el préstamo de {prestamo[0]} por el libro '{prestamo[2]}'? (s/n): ").lower()
            if confirmacion == "s":
                prestamos.pop(nro)
                print("Préstamo eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
        else:
            print("Número de préstamo inválido.")
    else:
        print("Debe ingresar un número válido.")
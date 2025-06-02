from datetime import datetime, date, time, timedelta
from funciones_utiles import buscar_nombre_usuario, limpiar_consola, encontrar_id_usuario, buscar_fila_libro
from modulo_libros import imprimir_libros

def crud_prestamos(): # Prestamos utilizando Tuplas
    prestamos = [
        ("Facu", 133185723, 'El principito', 'L002', "Antoine de Saint-Exupéry", 'Emecé', 1300, date.today(), (date.today() + timedelta(weeks=-0.2)), "Vencido"),
        ("Facu", 133185723, '1984', 'L004', "George Orwell", 'Destino', 5400, date.today(), (date.today() + timedelta(weeks=0.5)), "En Curso")
    ]
    return prestamos

def crear_prestamos(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual, permisos_usuario_actual):  # Crea el préstamo utilizando los datos del usuario logueado
    while True:
        libros_disponibles = [libro for libro in libros if libro[3] > 0]    # Crea lista por comprensión con los libros disponibles

        if not libros_disponibles:  # Verifica que haya libros dispo
            print("\nNo hay libros disponibles para préstamo.\n")
            return

        print("\n| Libros disponibles para préstamo |\n")
        print(f"{'Nº':<4} {'Nombre':<35} {'Código':<8} {'Autor':<25} {'Stock':<7} {'Editorial':<20}")
        print("-" * 125)

        for i, libro in enumerate(libros_disponibles, start=1):
            nombre, codigo, autor, stock, editorial = libro
            print(f"{i:<4} {nombre:<35} {codigo:<8} {autor:<25} {stock:<7} {editorial:<20}")

        print("-" * 125)

        try:
            opcion_libro = input("\nIngrese el número del libro que desea alquilar (o '0' para cancelar): ").strip()
            if opcion_libro == "0":
                print("\nOperación cancelada.\n")
                return

            indice_libro = int(opcion_libro) - 1
            if not (0 <= indice_libro < len(libros_disponibles)):
                print("\nNúmero fuera de rango. Intente nuevamente.\n")
                continue
        except ValueError:   
            print("\nEntrada inválida. Debe ingresar un número.\n")
            continue

        libro_seleccionado = libros_disponibles[indice_libro]
        fila_libro = libros.index(libro_seleccionado)

        if permisos_usuario_actual in ["admin"]:
            while True:
                try:
                    usuario_ingresado = input("\nIngrese el nombre de usuario de quien desea alquilar el libro (-1 para cancelar): ").strip() # Solo admins pueden hacer préstamos a otros
                    if usuario_ingresado == "-1":
                        return 
                    usuario_actual = buscar_nombre_usuario(usuarios_datos, usuario_ingresado)
                    if usuario_actual is None:
                        raise ValueError("Usuario no encontrado.")  
                    id_usuario_actual = encontrar_id_usuario(usuarios_datos, usuario_actual)
                    if id_usuario_actual is None:
                        raise ValueError("ID de usuario inválido.")
                    break
                except ValueError as err:   
                    print(f"\n{err}")
                    continue

        try:
            semanas_input = input("\nIngrese la cantidad de semanas que desea alquilar el libro (o '0' para cancelar): ").strip() # Determina la duración del préstamo
            if semanas_input == "0":
                print("\nOperación cancelada.\n")
                return

            semanas_a_alquilar = int(semanas_input)
            if semanas_a_alquilar <= 0:
                raise ValueError("Debe ingresar un número mayor que cero.")
        except ValueError as err:    
            print(f"\nEntrada inválida: {err}\n")
            continue

        nombre_libro = libro_seleccionado[0]
        id_libro = libro_seleccionado[1]
        autor_libro = libro_seleccionado[2]
        editorial = libro_seleccionado[4]
        precio = 1000 * (semanas_a_alquilar / 10)

        fecha_de_creacion = date.today()
        fecha_de_vencimiento = date.today() + timedelta(weeks=semanas_a_alquilar)

        print("\n\nLos datos del préstamo son: ")
        print(f"{usuario_actual} | {id_usuario_actual} | {nombre_libro} | {id_libro} | {autor_libro} | {editorial} | ${precio:.2f} | {estado_prestamo(fecha_de_vencimiento)}")
        print(f"\nFecha de inicio: {fecha_de_creacion}")
        print(f"Fecha de vencimiento: {fecha_de_vencimiento}\n")
        print("1. Confirmar los datos del préstamo")
        print("2. Cancelar el préstamo")

        opcion = input(f"Ingrese la opción que desea utilizar (-1 para volver al menu de {permisos_usuario_actual}): ").strip()
        if opcion == "1":
            prestamo = (
                usuario_actual,
                id_usuario_actual,
                nombre_libro,
                id_libro,
                autor_libro,
                editorial,
                precio,
                fecha_de_creacion,
                fecha_de_vencimiento,
                estado_prestamo(fecha_de_vencimiento)
            )
            prestamos.append(prestamo)
            libros[fila_libro][3] -= 1
            limpiar_consola()
            print("Se ha creado el préstamo exitosamente")
            return
        elif opcion == "2":
            print("\nPréstamo cancelado.\n")
            return
        elif opcion.strip() == "-1":
            return
        else:
            print("\nLa opción ingresada es inválida.\n")

def estado_prestamo(fecha_vencimiento):   # Define el estado del préstamo
    if fecha_vencimiento < date.today():
        return "Vencido"
    else:
        return "En curso"

def cambio_estado_inicio(prestamos):   
    for i in range(len(prestamos)):
        fila = prestamos[i]
        nueva_fila = fila[:-1] + (estado_prestamo(fila[8]),)
        prestamos[i] = nueva_fila

def imprimir_prestamos(prestamos, filtro="todos"):
    limpiar_consola()
    if not prestamos:
        print("| No hay préstamos registrados |")
        return

    print(f"|{'Listado de Préstamos':-^190}|")
    print(f"{'N°':<4}{'Usuario':<15}{'DNI':<12}{'Libro':<25}{'Código':<8}{'Autor':<25}{'Editorial':<15}{'Precio':<10}{'Inicio':<12}{'Vencimiento':<14}{'Estado':<10}")
    print("-" * 190)

    hoy = date.today()
    contador = 0

    for i, prestamo in enumerate(prestamos, 1):
        usuario, dni, libro, codigo, autor, editorial, precio, fecha_inicio, fecha_vencimiento, estado_original = prestamo

        if estado_original == "Devuelto":
            estado_actual = "Devuelto"
        else:
            estado_actual = estado_prestamo(fecha_vencimiento)

        dias_restantes = (fecha_vencimiento - hoy).days
        color = "\033[0m"
        mostrar = False  # Por defecto no se muestran, solo si cumplen con el filtro

        # ---------------------- FILTRO ----------------------
        if filtro == "todos":
            mostrar = True
        elif filtro == "devuelto" and estado_original == "Devuelto":
            mostrar = True
        elif filtro == "vencido" and estado_actual == "Vencido":
            mostrar = True
        elif filtro == "en curso" and estado_actual == "En curso":
            mostrar = True
        elif filtro == "por vencer" and estado_actual == "En curso" and dias_restantes <= 3:
            mostrar = True

        # COLORES
        if estado_actual == "Devuelto":
            color = "\033[94m"  # Azul
        elif estado_actual == "Vencido":
            color = "\033[91m"  # Rojo
        elif dias_restantes <= 3 and estado_actual == "En curso":
            color = "\033[93m"  # Amarillo
        else:
            color = "\033[92m"  # Verde

        # Mostrar si cumple filtro
        if mostrar:
            contador += 1
            print(f"{contador:<4}{usuario:<15}{dni:<12}{libro:<25}{codigo:<8}{autor:<25}{editorial:<15}${precio:<9.2f}{fecha_inicio.strftime('%d/%m/%Y'):<12}{fecha_vencimiento.strftime('%d/%m/%Y'):<14}{color}{estado_actual:<10}\033[0m")

    if contador == 0:
        print("No se encontraron préstamos según el filtro aplicado.")

    print("-" * 190)

def ver_prestamos_con_filtro(prestamos): # Añade un filtro según el estado del préstamo
    limpiar_consola()
    print(f"|{'Ver Préstamos':-^50}|")
    print("1. Ver todos los préstamos")
    print("2. Ver sólo préstamos en curso")
    print("3. Ver sólo préstamos vencidos")
    print("4. Ver préstamos próximos a vencer (3 días o menos)")
    print("5. Ver préstamos devueltos")
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
    elif opcion == "5":
        imprimir_prestamos(prestamos, filtro="devuelto")
    elif opcion == "9":
        return
    else:
        print("Opción inválida.")

def actualizar_prestamo(prestamos, libros):
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
            print("1. Fecha de vencimiento")
            print("2. Devolver libro")
            print("3. Volver al menu anterior")
            opcion = input("Ingrese opción: ")
            opcion = opcion.strip()
            if opcion == "1":
                semanas_extra = input("Ingrese cuántas semanas desea extender el préstamo (-1 para cancelar): ")
                if semanas_extra.strip() == "-1":
                    return
                elif semanas_extra.isnumeric() and int(semanas_extra) > 0:
                    semanas_extra = int(semanas_extra)
                    fila = prestamos[nro]

                    fila_del_libro = buscar_fila_libro(libros, nombre=prestamos[nro][2])

                    if fila_del_libro is None:
                        print("No se encontró el libro.")
                        return

                    precio_total_libro = fila[6]  #  ya no busca precio de libros sino de prestamos
                    precio = precio_total_libro * (semanas_extra / 10)
                    precio = precio + fila[6] 

                    nueva_fecha = fila[8] + timedelta(weeks=semanas_extra)
                    nueva_fila = fila[:6] + (precio, fila[7], nueva_fecha, estado_prestamo(nueva_fecha))
                    prestamos[nro] = nueva_fila

                    print("Fecha de vencimiento actualizada correctamente.")
                else:
                    print("Cantidad de semanas inválida.")    
            elif opcion == "2":
                # Devuelve el libro
                fila = prestamos[nro]
                
                # Verificar si ya estaba devuelto
                if fila[9] == "Devuelto":
                    print("El préstamo ya fue devuelto anteriormente.")
                    return

                # Aumenta stock del libro
                fila_del_libro = buscar_fila_libro(libros, nombre=fila[2])
                if fila_del_libro is not None:
                    libros[fila_del_libro][3] += 1

                # Actualiza estado del préstamo a Devuelto
                nueva_fila = fila[:-1] + ("Devuelto",)
                prestamos[nro] = nueva_fila

                print("El préstamo se ha devuelto correctamente.")
            elif opcion == "3":
                return
            else:
                print("Opción inválida.")
        else:
            print("Número de préstamo inválido.")
    else:
        print("Debe ingresar un número válido.")

def eliminar_prestamo(prestamos, libros):   # Elimina un préstamo existente
    limpiar_consola()
    if not prestamos:   # Verifica que existan prestamos (Hay un elemento dentro de prestamos)
        print("| No hay préstamos para eliminar |")
        return

    imprimir_prestamos(prestamos)

    nro = input("\nIngrese el número de préstamo que desea eliminar (-1 para cancelar): ")
    if nro.strip() == "-1":
        return
    elif nro.isnumeric():
        nro = int(nro) - 1
        if 0 <= nro < len(prestamos):
            prestamo = prestamos[nro]
            confirmacion = input(f"\n¿Confirma eliminar el préstamo de {prestamo[0]} por el libro '{prestamo[2]}'? (s/n) (-1 para cancelar): ").lower()
            if confirmacion == "s":
                # Buscar el libro en el inventario y aumentar su stock
                id_libro_prestamo = prestamo[3]  # Código del libro del préstamo
                for libro in libros:
                    if libro[1] == id_libro_prestamo:
                        libro[3] += 1  # Aumenta el stock en 1
                        break

                prestamos.pop(nro)  # Elimina el préstamo
                print("\nPréstamo eliminado correctamente. El stock del libro ha sido actualizado.")
            elif confirmacion.strip() == "-1":
                return
            else:
                print("\nEliminación cancelada.")
        else:
            print("\nNúmero de préstamo inválido.")
    else:
        print("\nDebe ingresar un número válido.")

def ver_mis_prestamos(prestamos, usuario_actual):  # Imprime préstamos según el ID del usuario logueado
    limpiar_consola()
    mis_prestamos = [p for p in prestamos if p[0] == usuario_actual]    # Filtra la lista para obtener solo los que su primer valor (usuario) coincide con el usuario_actual

    if not mis_prestamos:
        print("| Usted no tiene préstamos registrados |")
        return

    print(f"|{'Sus Préstamos':-^190}|")
    print(f"{'N°':<4}{'Libro':<25}{'Código':<8}{'Autor':<25}{'Editorial':<15}{'Precio':<10}{'Inicio':<12}{'Vencimiento':<14}{'Estado':<10}")
    print("-" * 190)

    hoy = date.today()

    for i, prestamo in enumerate(mis_prestamos, 1):         # Recorremos la lista de préstamos del usuario, empezando el índice desde 1
        _, _, libro, codigo, autor, editorial, precio, fecha_inicio, fecha_vencimiento, _ = prestamo   # Desempaquetamos los valores del préstamo (ignoramos los campos que no usamos con '_')
        estado_actual = estado_prestamo(fecha_vencimiento)

        dias_restantes = (fecha_vencimiento - hoy).days

        color = "\033[0m"        # Inicializamos el color (por defecto sin color)
        if estado_actual == "Vencido":
            color = "\033[91m"
        elif dias_restantes <= 3:
            color = "\033[93m"
        else:
            color = "\033[92m"

        print(f"{i:<4}{libro:<25}{codigo:<8}{autor:<25}{editorial:<15}${precio:<9.2f}{fecha_inicio.strftime('%d/%m/%Y'):<12}{fecha_vencimiento.strftime('%d/%m/%Y'):<14}{color}{estado_actual:<10}\033[0m")
        # Se pone el color con los marcadores {} del f-string, y se resetea al final con \033[0m
    print("-" * 190)
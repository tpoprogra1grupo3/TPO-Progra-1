from modulo_libros import añadir_libro, eliminar_libro, imprimir_libros, buscar_libro, actualizar_libro
from funciones_utiles import limpiar_consola, titulo, cambiar_rol
from Log_y_Sign_in.login import iniciar_sesion
from Log_y_Sign_in.sign_in import crear_usuario
from prestamos import crear_prestamos, ver_prestamos_con_filtro, actualizar_prestamo, eliminar_prestamo, ver_mis_prestamos

def menu_inicio(usuarios_datos, libros, prestamos):  # Menu de registro y login
    while True:
        limpiar_consola()
        print(f"\n{'=' * 60}")
        print(f"{'Bienvenido al sistema de Biblioteca Bineder'.center(60)}")
        print(f"{'=' * 60}\n")

        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("0. Salir\n")

        opcion = input("Seleccione una opción:\n> ").strip()

        if opcion == "1":
            limpiar_consola()
            titulo(1)
            crear_usuario(usuarios_datos)
            input("\nPresione ENTER para continuar...")
        elif opcion == "2":
            limpiar_consola()
            titulo(2)
            rol, usuario_actual, id_usuario_actual = iniciar_sesion(usuarios_datos)  # Se guarda el usuario y el ID para uso posterior.
            limpiar_consola()
            print(f"Usted tiene el rol de {rol}")

            if rol == "admin":
                resultado = menu_admin(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual)
            elif rol == "socio":
                resultado = menu_socio(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual)
            elif rol == "empleado":
                resultado = menu_empleado(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual)

            if resultado == "volver_inicio":
                continue
            input("\nPresione ENTER para continuar...")
        elif opcion == "0":
            print("\nGracias por utilizar el sistema. ¡Hasta luego!")
            break
        else:
            print("\nLa opción ingresada no es válida.")
            input("Presione ENTER para intentarlo de nuevo...")

def mostrar_menu(titulo_menu, opciones):  # Permite el cierre de sesión desde los distintos menu y submenu.
    while True:
        limpiar_consola()
        print(f"\n{'=' * 50}")
        print(titulo_menu.center(50))
        print(f"{'=' * 50}\n")

        for numero, opcion in sorted(opciones.items()):
            print(f"{numero}. {opcion['texto']}")

        opcion = input("\nSeleccione una opción:\n> ").strip()

        if opcion == "9" or (opcion in opciones and opciones[opcion]["accion"] == "volver_inicio"):
            return "volver_inicio"

        if opcion in opciones:
            if opciones[opcion]["accion"] == "volver":
                break
            else:
                limpiar_consola()
                resultado = opciones[opcion]["accion"]()
                if resultado == "volver_inicio":
                    return "volver_inicio"
                input("\nPresione ENTER para continuar...")
        else:
            print("\nLa opción ingresada no es válida.")
            input("Presione ENTER para intentarlo de nuevo...")

def menu_admin(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual):   # Menu Principal Vista Admin
    while True:
        opciones_admin = {
            "0": {"texto": "Dar rol de empleado", "accion": lambda: cambiar_rol(usuarios_datos)},
            "1": {"texto": "Inventario", "accion": lambda: submenu_inventario(libros)},
            "2": {"texto": "Préstamos", "accion": lambda: submenu_prestamos(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual)},
            "9": {"texto": "Cerrar sesión", "accion": "volver"}
        }
        resultado = mostrar_menu("Bienvenido al menú de Admin", opciones_admin)
        if resultado == "volver_inicio":
            return "volver_inicio"

def menu_empleado(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual):  # Menu Principal Vista Empleado
    while True:
        opciones_empleado = {
            "1": {"texto": "Inventario", "accion": lambda: submenu_inventario(libros)},
            "2": {"texto": "Préstamos", "accion": lambda: submenu_prestamos(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual)},
            "9": {"texto": "Cerrar sesión", "accion": "volver"}
        }
        resultado = mostrar_menu("Bienvenido al menú de Empleado", opciones_empleado)
        if resultado == "volver_inicio":
            return "volver_inicio"

def menu_socio(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual):   # Menu Principal Vista Socio
    while True:
        opciones_socio = {
            "1": {"texto": "Mostrar inventario actual", "accion": lambda: imprimir_libros(libros)},
            "2": {"texto": "Buscar libro específico", "accion": lambda: buscar_libro(libros)},
            "3": {"texto": "Crear un préstamo", "accion": lambda: crear_prestamos(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual)},
            "4": {"texto": "Ver mis préstamos", "accion": lambda: ver_mis_prestamos(prestamos, usuario_actual)},
            "9": {"texto": "Cerrar sesión", "accion": "volver"}
        }
        resultado = mostrar_menu("Bienvenido al menú de Socio", opciones_socio)
        if resultado == "volver_inicio":
            return "volver_inicio"

def submenu_inventario(libros):   # Submenu Inventario
    opciones_inventario = {
        "1": {"texto": "Añadir un libro al inventario", "accion": lambda: añadir_libro(libros)},
        "2": {"texto": "Eliminar libro", "accion": lambda: eliminar_libro(libros)},
        "3": {"texto": "Mostrar inventario actual", "accion": lambda: imprimir_libros(libros)},
        "4": {"texto": "Buscar libro específico", "accion": lambda: buscar_libro(libros)},
        "5": {"texto": "Actualizar libro", "accion": lambda: actualizar_libro(libros)},
        "8": {"texto": "Volver al menú anterior", "accion": "volver"},
        "9": {"texto": "Cerrar sesión y volver al menú principal", "accion": "volver_inicio"}
    }
    resultado = mostrar_menu("Submenú Inventario", opciones_inventario)
    if resultado == "volver_inicio":
        return "volver_inicio"

def submenu_prestamos(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual):  # Submenu Préstamos
    opciones_prestamos = {
        "1": {"texto": "Crear un préstamo", "accion": lambda: crear_prestamos(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual)},
        "2": {"texto": "Ver préstamos existentes", "accion": lambda: ver_prestamos_con_filtro(prestamos)},
        "3": {"texto": "Actualizar un préstamo", "accion": lambda: actualizar_prestamo(prestamos)},
        "4": {"texto": "Eliminar un préstamo", "accion": lambda: eliminar_prestamo(prestamos, libros)},
        "8": {"texto": "Volver al menú anterior", "accion": "volver"},
        "9": {"texto": "Cerrar sesión y volver al menú principal", "accion": "volver_inicio"}
    }
    resultado = mostrar_menu("Submenú Préstamos", opciones_prestamos)
    if resultado == "volver_inicio":
        return "volver_inicio"
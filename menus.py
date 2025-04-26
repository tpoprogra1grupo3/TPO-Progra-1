from modulo_libros import añadir_libro, eliminar_libro, imprimir_libros, buscar_libro, actualizar_libro
from funciones_utiles import limpiar_consola, titulo, cambiar_rol
from Log_y_Sign_in.login import iniciar_sesion
from Log_y_Sign_in.sign_in import crear_usuario
from prestamos import crear_prestamos, ver_prestamos_con_filtro, actualizar_prestamo, eliminar_prestamo

def menu_inicio(usuarios_datos, libros, prestamos):
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
            permisos = iniciar_sesion(usuarios_datos)
            limpiar_consola()
            print(f"Usted tiene el rol de {permisos}")

            if permisos == "admin":
                menu_admin(usuarios_datos, libros, prestamos)
            elif permisos == "socio":
                menu_socio(usuarios_datos, libros, prestamos)
            elif permisos == "empleado":
                menu_empleado(usuarios_datos, libros, prestamos)

            input("\nPresione ENTER para continuar...")
        elif opcion == "0":
            print("\nGracias por utilizar el sistema. ¡Hasta luego!")
            break
        else:
            print("\nLa opción ingresada no es válida.")
            input("Presione ENTER para intentarlo de nuevo...")

def mostrar_menu(titulo_menu, opciones):
    while True:
        limpiar_consola()
        print(f"\n{'=' * 50}")
        print(f"{titulo_menu.center(50)}")
        print(f"{'=' * 50}\n")

        for numero, opcion in sorted(opciones.items()):
            print(f"{numero}. {opcion['texto']}")

        print("\nSeleccione una opción:")
        opcion = input("> ").strip()

        if opcion in opciones:
            if opciones[opcion]["accion"] == "volver":
                break
            else:
                limpiar_consola()
                opciones[opcion]["accion"]()
                input("\nPresione ENTER para continuar...")
        else:
            print("\nLa opción ingresada no es válida.")
            input("Presione ENTER para intentarlo de nuevo...")

def menu_admin(usuarios_datos, libros, prestamos):
    opciones_admin = {
        "0": {"texto": "Dar rol de empleado", "accion": lambda: cambiar_rol(usuarios_datos)},
        "1": {"texto": "Inventario", "accion": lambda: submenu_inventario(libros)},
        "2": {"texto": "Préstamos", "accion": lambda: submenu_prestamos(usuarios_datos, libros, prestamos)},
        "9": {"texto": "Cerrar sesión", "accion": "volver"}
    }
    mostrar_menu("Bienvenido al menú de Admin", opciones_admin)

def menu_empleado(usuarios_datos, libros, prestamos):
    opciones_empleado = {
        "1": {"texto": "Inventario", "accion": lambda: submenu_inventario(libros)},
        "2": {"texto": "Préstamos", "accion": lambda: submenu_prestamos(usuarios_datos, libros, prestamos)},
        "9": {"texto": "Cerrar sesión", "accion": "volver"}
    }
    mostrar_menu("Bienvenido al menú de Empleado", opciones_empleado)

def menu_socio(usuarios_datos, libros, prestamos):
    opciones_socio = {
        "1": {"texto": "Mostrar inventario actual", "accion": lambda: imprimir_libros(libros)},
        "2": {"texto": "Buscar libro específico", "accion": lambda: buscar_libro(libros)},
        "3": {"texto": "Crear un préstamo", "accion": lambda: crear_prestamos(usuarios_datos, libros, prestamos)},
        "9": {"texto": "Cerrar sesión", "accion": "volver"}
    }
    mostrar_menu("Bienvenido al menú de Socio", opciones_socio)

def submenu_inventario(libros):
    opciones_inventario = {
        "1": {"texto": "Añadir un libro al inventario", "accion": lambda: añadir_libro(libros)},
        "2": {"texto": "Eliminar libro", "accion": lambda: eliminar_libro(libros)},
        "3": {"texto": "Mostrar inventario actual", "accion": lambda: imprimir_libros(libros)},
        "4": {"texto": "Buscar libro específico", "accion": lambda: buscar_libro(libros)},
        "5": {"texto": "Actualizar libro", "accion": lambda: actualizar_libro(libros)},
        "9": {"texto": "Volver al menú anterior", "accion": "volver"}
    }
    mostrar_menu("Submenú Inventario", opciones_inventario)

def submenu_prestamos(usuarios_datos, libros, prestamos):
    opciones_prestamos = {
        "1": {"texto": "Crear un préstamo", "accion": lambda: crear_prestamos(usuarios_datos, libros, prestamos)},
        "2": {"texto": "Ver préstamos existentes", "accion": lambda: ver_prestamos_con_filtro(prestamos)},
        "3": {"texto": "Actualizar un préstamo", "accion": lambda: actualizar_prestamo(prestamos)},
        "4": {"texto": "Eliminar un préstamo", "accion": lambda: eliminar_prestamo(prestamos)},
        "9": {"texto": "Volver al menú anterior", "accion": "volver"}
    }
    mostrar_menu("Submenú Préstamos", opciones_prestamos)
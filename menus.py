from modulo_libros import añadir_libro, eliminar_libro, imprimir_libros, buscar_libro, actualizar_libro
from funciones_utiles import limpiar_consola, titulo, mostrar_mi_id      #, cambiar_rol
from Log_y_Sign_in.login import iniciar_sesion
from Log_y_Sign_in.sign_in import crear_usuario, mostrar_usuarios, eliminar_usuarios_por_id, eliminar_mi_usuario, cambiar_mail
from prestamos import crear_prestamos, ver_prestamos_con_filtro, actualizar_prestamo, eliminar_prestamo, ver_mis_prestamos

def menu_inicio(usuarios_datos, libros, prestamos):  # Menu de registro y login
    while True:
        limpiar_consola()
        print(f"\n{'=' * 60}")
        print(f"{'Bienvenido al sistema de Biblioteca Bineder'.center(60)}")
        print(f"{'=' * 60}\n")

        print("1. Registrarse")
        print("2. Iniciar sesión/Cambiar contraseña")
        print("0. Salir\n")

        opcion = input("Seleccione una opción:\n> ").strip()

        if opcion == "1":
            limpiar_consola()
            titulo(1)
            crear_usuario(usuarios_datos)     # La opcion volver da un return para finalizar la iteracion actual
            input("\nPresione ENTER para continuar...")
        
        elif opcion == "2":
            limpiar_consola()
            titulo(2)
            rol, usuario_actual, id_usuario_actual = iniciar_sesion(usuarios_datos)  # Se guarda el usuario y el ID para uso posterior.
            if usuario_actual == "Volver":
                continue        # Devuelve al menu de inicio (No se ejecuta ningun menu del rol correspondiente)
            
            limpiar_consola()
            print(f"Usted tiene el rol de {rol}")
            if rol == "admin":
                resultado = menu_admin(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual)
            elif rol == "socio":
                resultado = menu_socio(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual)

            if resultado == "volver_inicio":
                continue
            input("\nPresione ENTER para continuar...")
        elif opcion == "0":
            print("\nGracias por utilizar el sistema. ¡Hasta luego!")
            break
        else:
            print("\nLa opción ingresada no es válida.")
            input("Presione ENTER para intentarlo de nuevo...")

def mostrar_menu(titulo_menu, opciones):  # Generaliza el mostrado de menús con diccionarios 
    while True:
        limpiar_consola()
        print(f"\n{'=' * 50}")
        print(titulo_menu.center(50))      # Imprime el título del menú dado
        print(f"{'=' * 50}\n")


        for numero, opcion in sorted(opciones.items()): # Imprime las opciones en orden (forma abreviada de hacerlo)
            print(f"{numero}. {opcion['texto']}")


        opcion = input("\nSeleccione una opción:\n> ").strip()


        if opcion == "9" or (opcion in opciones and opciones[opcion]["accion"] == "volver_inicio"):     # Evita que intente ejecutarse una función lambda si tengo str en esa pos.
            return "volver_inicio"                                                    # Permite el cierre de sesión desde los distintos menu y submenu!!!


        if opcion in opciones:
            if opciones[opcion]["accion"] == "volver":     # Rompe el ciclo para que se repita el menú previo
                break
            else:
                limpiar_consola()
                resultado = opciones[opcion]["accion"]()  # Esto ejecuta una función, osea si fuese un str en lugar de un lambda, nos da error. Por eso el if de arriba
                if resultado == "volver_inicio":
                    return "volver_inicio"                 # Se hace una cadena de returns que nos llevan al primer menú de todos
                input("\nPresione ENTER para continuar...")
        else:
            print("\nLa opción ingresada no es válida.")
            input("Presione ENTER para intentarlo de nuevo...")


def menu_admin(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual):   # Menu Principal Vista Admin
    while True:
        opciones_admin = {
            "1": {"texto": "Bibloteca", "accion": lambda: submenu_bibloteca(libros)},
            "2": {"texto": "Préstamos", "accion": lambda: submenu_prestamos(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual,"admin")},
            "3": {"texto": "Mostrar info de usuarios del sistema", "accion": lambda: mostrar_usuarios(usuarios_datos)},
            "4": {"texto": "Eliminar usuarios por Id", "accion":lambda: eliminar_usuarios_por_id(usuarios_datos,id_usuario_actual)},
            "9": {"texto": "Cerrar sesión", "accion": "volver"}
        }
        resultado = mostrar_menu("Bienvenido al menú de Admin", opciones_admin)
        if resultado == "volver_inicio":
            return "volver_inicio"

def menu_socio(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual):   # Menu Principal Vista Socio
    while True:
        opciones_socio = {
            "1": {"texto": "Mostrar libros disponibles actualmente", "accion": lambda: imprimir_libros(libros)},
            "2": {"texto": "Buscar libro específico", "accion": lambda: buscar_libro(libros)},
            "3": {"texto": "Crear un préstamo", "accion": lambda: crear_prestamos(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual,"socio")},
            "4": {"texto": "Ver mis préstamos", "accion": lambda: ver_mis_prestamos(prestamos, usuario_actual)},
            "5": {"texto": "Ver mi ID", "accion": lambda: mostrar_mi_id(usuario_actual, id_usuario_actual)},
            "6": {"texto": "Eliminar mi usuario", "accion": lambda: eliminar_mi_usuario(usuarios_datos, usuario_actual)},
            "7": {"texto": "Cambiar mi mail", "accion": lambda: cambiar_mail(usuarios_datos, usuario_actual)},
            "9": {"texto": "Cerrar sesión", "accion": "volver"}
        }
        resultado = mostrar_menu("Bienvenido al menú de Socio", opciones_socio)
        if resultado == "volver_inicio":
            return "volver_inicio"

def submenu_bibloteca(libros):   # Submenu bibloteca
    opciones_bibloteca = {
        "1": {"texto": "Añadir un libro a la bibloteca", "accion": lambda: añadir_libro(libros)},
        "2": {"texto": "Eliminar libro", "accion": lambda: eliminar_libro(libros)},
        "3": {"texto": "Mostrar libros disponibles actualmente", "accion": lambda: imprimir_libros(libros)},
        "4": {"texto": "Buscar libro específico", "accion": lambda: buscar_libro(libros)},
        "5": {"texto": "Actualizar libro", "accion": lambda: actualizar_libro(libros)},
        "8": {"texto": "Volver al menú anterior", "accion": "volver"},
        "9": {"texto": "Cerrar sesión y volver al menú principal", "accion": "volver_inicio"}
    }
    resultado = mostrar_menu("Submenú Bibloteca", opciones_bibloteca)     
    if resultado == "volver_inicio":
        return "volver_inicio"

def submenu_prestamos(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual,permisos_usuario_actual):  # Submenu Préstamos
    opciones_prestamos = {
        "1": {"texto": "Crear un préstamo", "accion": lambda: crear_prestamos(usuarios_datos, libros, prestamos, usuario_actual, id_usuario_actual, permisos_usuario_actual)},
        "2": {"texto": "Ver préstamos existentes", "accion": lambda: ver_prestamos_con_filtro(prestamos)},
        "3": {"texto": "Actualizar un préstamo", "accion": lambda: actualizar_prestamo(prestamos,libros)},
        "4": {"texto": "Eliminar un préstamo", "accion": lambda: eliminar_prestamo(prestamos, libros)},
        "8": {"texto": "Volver al menú anterior", "accion": "volver"},
        "9": {"texto": "Cerrar sesión y volver al menú principal", "accion": "volver_inicio"}
    }
    resultado = mostrar_menu("Submenú Préstamos", opciones_prestamos)
    if resultado == "volver_inicio":
        return "volver_inicio"
from inventario import añadir_libro,eliminar_libro,imprimir_libros,buscar_libro
from funciones_utiles import limpiar_consola, titulo, cambiar_rol
from Log_y_Sign_in.login import iniciar_sesion
from Log_y_Sign_in.sign_in import crear_usuario


def menu_inicio(usuarios_datos,libros):                      # LogIn/SignIn
    interruptor = True
    while interruptor:
        limpiar_consola()
        print(f"|{"Bienvenido al sistema de Bibloteca Bineder":-^60}|", end="\n\n")
        print("1. Registrarse")
        print("2. Iniciar sesion\n")
        while True:
            print("Escriba el numero correspondiente a la opción que desea utilizar: ")
            opcion = input()
            if opcion == "1" or opcion == "2":
                opcion = int(opcion)
                break
            else:
                print("La opción ingresada no es válida")
        
        # SERÍA IDEAL PASAR LAS FUNCIONES DEL MENU INICIO A OTRO ARCHIVO 
        print(end="\n")
        if opcion == 1:
            titulo(opcion)
            crear_usuario(usuarios_datos)
        elif opcion == 2:
            titulo(opcion)
            permisos = iniciar_sesion(usuarios_datos)
            limpiar_consola()
            print(f"Usted tiene el rol de {permisos}")
            interruptor = False
            if permisos=="admin":
                menu_admin(usuarios_datos,libros) 
            elif permisos=="socio":
                menu_socio(usuarios_datos,libros) 
            elif permisos=="empleado":
                menu_empleado(usuarios_datos,libros)

def menu_admin(usuarios_datos,libros):
    bandera = True
    while bandera:
        limpiar_consola()
        print(f"|{"Bienvenido al menú de admin":-^45}|", end="\n\n")
        print("0. Dar rol de empleado")
        print("1. Añadír un libro al inventario")
        print("2. Eliminar libro")
        print("3. Mostrar inventario actual")
        print("4. Buscar libro específico")
        print("9. Para cerrar sesión")
        opcion_admin = input("Escriba el numero correspondiente a la opción que desea utilizar: ")
        if opcion_admin.isnumeric and len(opcion_admin)== 1:
            opcion_admin = int(opcion_admin)
            if opcion_admin==1:
                añadir_libro(libros)
            elif opcion_admin==2:
                eliminar_libro(libros)
            elif opcion_admin==3:
                imprimir_libros(libros)
            elif opcion_admin==4:
                buscar_libro(libros)
            elif opcion_admin==9:
                bandera = False
                menu_inicio(usuarios_datos,libros)
            elif opcion_admin==0:
                cambiar_rol(usuarios_datos)
        else:
            print("La opción ingresada es inválida\n")

def menu_empleado(usuarios_datos,libros):
    bandera = True
    while bandera:
        limpiar_consola()
        print(f"|{"Bienvenido al menú de Empleado":-^45}|", end="\n\n")
        print("1. Añadír un libro al inventario")
        print("2. Eliminar libro")
        print("3. Mostrar inventario actual")
        print("4. Buscar libro específico")
        print("9. Para cerrar sesión")
        opcion_empleado = input("Escriba el numero correspondiente a la opción que desea utilizar: ")
        if opcion_empleado.isnumeric and len(opcion_empleado)== 1:
            opcion_empleado = int(opcion_empleado)
            if opcion_empleado==1:
                añadir_libro(libros)
            elif opcion_empleado==2:
                eliminar_libro(libros)
            elif opcion_empleado==3:
                imprimir_libros(libros)
            elif opcion_empleado==4:
                buscar_libro(libros)
            elif opcion_empleado==9:
                bandera = False
                menu_inicio(usuarios_datos,libros)
        else:
            print("La opción ingresada es inválida\n")
    
def menu_socio(usuarios_datos,libros):
    print(f"|{"Bienvenido al menú de socio":-^45}|", end="\n\n")
    EJEMPLO = input("")

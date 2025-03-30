import random
import os
from inventario import añadir_libro,eliminar_libro,imprimir_libros,biblioteca

def menu_inicio(usuarios_datos,libros):                      # LogIn/SignIn
    interruptor = True
    while interruptor:
        limpiar_consola()
        print(usuarios_datos)
        print(f"|{"Bienvenido al sistema de Bibloteca Bineder":-^60}|", end="\n\n")
        print("1. Registrarse")
        print("2. Iniciar sesion\n")
        print("Escriba el numero correspondiente a la opción que desea utilizar: ")
        opcion = int(input())
    
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
            elif permisos=="cliente":
                menu_cliente(usuarios_datos,libros) 

def titulo(opcion):
    if opcion==1:
        limpiar_consola()
        print(f"||{" Usted esta creando un Usuario ":=^60}||", end="\n\n")
    else:
        limpiar_consola()
        print("Usted a Iniciado Sesion!!")

def crear_contraseña():                 # Verifica que la contraseña cumpla con los parámetros de seguridad
    longitud_min_contraseñas = 5         
    print(f"\nRecuerde que su contraseña debe tener al menos:")
    print(f"\t-{longitud_min_contraseñas} dígitos")
    print(f"\t-Debe tener por lo menos 1 carácter especial")
    print(f"\t-No debe tener espacios vacíos (No se puede dejar huecos entre caracteres)")
    while True:
        contraseña = input("\nIngrese una contraseña: ")
        if contraseña.isalnum() == False: # Verifica que hayan caracteres especiales
            if len(contraseña)>= 5:       # Verifica que tenga 5 o más caracteres
                if contraseña.count(" ") == 0:  # Verifica que no hayan espacios 
                    return contraseña
        print("Contraseña inválida")

def crear_nombre_usuario(usuarios_datos): 
    while True:
        usuario = input("Ingrese el nombre de usuario que desea utilizar: ")
        validez = buscar_nombre_usuario(usuarios_datos,usuario) # Verifica que no esté ocupado
        if validez == None:             # Si esta ocupado devuelve True, sino None
            return usuario
        print("Usuario inválido/Ya en uso")

def generar_id_usuario(usuarios_datos,dni):
    while True:    
        cadena_delantera = ""
        cadena_trasera = ""
        for i in range(0,3):
            cadena_delantera = cadena_delantera + str(random.randint(0,9))
            cadena_trasera = cadena_trasera + str(random.randint(0,9))
        id = cadena_delantera + str(dni) + cadena_trasera
        if validar_id(usuarios_datos,id)==True: # Chequea que no este repetido el id
            return id
        
def validar_id(usuarios_datos,id):
    if len(usuarios_datos) != 0:
        for fila in usuarios_datos:
            if fila[4] == id:           # Se fija fila por fila que nadie tenga el id a crear
                return False
        return True
    else:
        return True 
    
def crear_usuario(usuarios_datos):
    usuario = crear_nombre_usuario(usuarios_datos)
    titulo(1)
    contraseña = crear_contraseña()     
    titulo(1)

    while True:                      # Validar que el dni tenga 3 dígitos
        dni = input("Ingrese los 3 últimos dígitos de su DNI: ")
        if len(dni) == 3:
            dni = int(dni)
            break
        else:
            print("DNI inválido")

    id = generar_id_usuario(usuarios_datos,dni)
    
    if len(usuarios_datos)==0:          # El usuario numero 0 es admin siempre                                   
        permisos = "admin"
    else:
        permisos = "cliente"
    
    usuarios_datos.append([usuario,contraseña,dni,permisos,id]) # Se agrega una fila con los datos del usuario, a la matriz que tiene a todos
    limpiar_consola()

    
def iniciar_sesion(usuarios_datos):
    bandera = True
    while bandera:
        usuario = input("Ingrese su nombre de usuario: ")
        fila = buscar_nombre_usuario(usuarios_datos,usuario) # Busca la lista de la matriz correspondiente al usuario
        if fila!=None:
            while bandera:
                contraseña = input("Ingrese su contraseña: ")
                if contraseña == usuarios_datos[fila][1]:    # Se válida que la contraseña ingresada sea la pertenenciente al usuario
                    return usuarios_datos[fila][3]          # Retorna el rol/rango del usuario
                else:
                    print("\nContraseña incorrecta\n") 
        else: 
            print("\nEse usuario no existe\n")

def buscar_nombre_usuario(usuarios_datos,usuario):
    for fila in range(0,len(usuarios_datos)):   
        if usuario == usuarios_datos[fila][0]:  # Mira fila a fila si el usuario existe en alguna lista de la matriz
            return fila                         # En caso de existir, devuelve la fila del usuario
        elif fila == len(usuarios_datos)-1:     
            return None                         # Caso contrario devuelve None





def menu_admin(usuarios_datos,libros):
    print(f"|{"Bienvenido al menú de admin":-^45}|", end="\n\n")
    print("1. Añadír un libro al inventario")
    print("2. Eliminar libro")
    print("3. Mostrar inventario actual")
    print("9. Para cerrar sesión")
    while True:
        opcion_admin = input("Escriba el numero correspondiente a la opción que desea utilizar: ")
        if opcion_admin != None and opcion_admin.isnumeric and len(opcion_admin)== 1:
            opcion_admin = int(opcion_admin)
            if opcion_admin==1:
                añadir_libro(libros)
            elif opcion_admin==2:
                eliminar_libro(libros)
            elif opcion_admin==3:
                imprimir_libros(libros)
            elif opcion_admin==9:
                menu_inicio(usuarios_datos,libros)
        else:
            print("La opción ingresada es inválida\n")
    

def menu_cliente(usuarios_datos,libros):
    print(f"|{"Bienvenido al menú de cliente":-^45}|", end="\n\n")
    EJEMPLO = input("")

def limpiar_consola(): # Vacía la consola
    os.system("cls")

def main():
    usuarios_datos = []                 # Inicializo la MATRIZ de usuarios
    libros = biblioteca()
    menu_inicio(usuarios_datos,libros)



main()                                  # Programa Principal
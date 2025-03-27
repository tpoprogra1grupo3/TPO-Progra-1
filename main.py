import random

def menu_inicio():                      # LogIn/SignIn
    print(f"|{"Bienvenido al sistema de Bibloteca Bineder":-^60}|", end="\n\n")
    print("1. Registrarse")
    print("2. Iniciar sesion\n")
    print("Escriba el numero correspondiente a la opción que desea utilizar: ")
    opcion = int(input())
    return opcion

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
    contraseña = crear_contraseña()     
    
    while True:                         # Validar que el dni tenga 3 dígitos
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
    print("\n¡Felicitaciones! Acaba de crear su usuario. Inicie sesión\n")
    print(usuarios_datos)
    
def iniciar_sesion(usuarios_datos):
    bandera = True
    while bandera:
        usuario = input("Ingrese su nombre de usuario: ")
        fila = buscar_nombre_usuario(usuarios_datos,usuario) # Busca la lista de la matriz correspondiente al usuario
        if fila!=None:
            while bandera:
                contraseña = input("Ingrese su contraseña: ")
                if contraseña == usuarios_datos[fila][1]:    # Se válida que la contraseña ingresada sea la pertenenciente al usuario
                    print(usuarios_datos)
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

def menu_admin():
    print(f"|{"Bienvenido al menú de admin":-^45}|", end="\n\n")

def menu_cliente():
    print(f"|{"Bienvenido al menú de cliente":-^45}|", end="\n\n")


def main():
    usuarios_datos = []                 # Inicializo la MATRIZ de usuarios
    
    while True:
        opcion_inicio = menu_inicio()
        print(end="\n")
        if opcion_inicio == 1:
            crear_usuario(usuarios_datos) 
        elif opcion_inicio == 2:
            permisos = iniciar_sesion(usuarios_datos)
            print(f"Usted tiene el rol de {permisos}")
            break    
    
    if permisos=="admin":
        menu_admin()
    elif permisos=="cliente":
        menu_cliente()



main()                                  # Programa Principal
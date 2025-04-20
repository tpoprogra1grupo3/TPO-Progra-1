from funciones_utiles import buscar_nombre_usuario, titulo, limpiar_consola
import random

def usuarios_de_base():
    usuarios_datos = [
    ['Juan', 'Hola!', '836', "admin", 156836921],
    ['Elian', '5555!', '856','admin', 527856776],
    ['Facu', '1234-', '185', 'socio', 133185723],
    ['Iair007', 'Messi@', '835','empleado', 111835221],
    ['Esteban', 'mentaaa#', '257','empleado', 290257618],
    ]

    return usuarios_datos

def crear_usuario(usuarios_datos):
    usuario = crear_nombre_usuario(usuarios_datos)
    titulo(1)
    contraseña = crear_contraseña()     
    titulo(1)

    while True:                      # Validar que el dni tenga 3 dígitos
        dni = input("Ingrese los 3 últimos dígitos de su DNI: ")
        if len(dni) == 3 and dni.isnumeric:
            dni = int(dni)
            break
        else:
            print("DNI inválido")

    id = generar_id_usuario(usuarios_datos,dni)
    
    if len(usuarios_datos)==0:          # El usuario numero 0 es admin siempre                                   
        permisos = "admin"
    else:
        permisos = "socio"
    
    usuarios_datos.append([usuario,contraseña,dni,permisos,id]) # Se agrega una fila con los datos del usuario, a la matriz que tiene a todos
    limpiar_consola() 

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
        
def crear_nombre_usuario(usuarios_datos): 
    while True:
        usuario = input("Ingrese el nombre de usuario que desea utilizar: ")
        if usuario.isalnum() == True:
            validez = buscar_nombre_usuario(usuarios_datos,usuario) # Verifica que no esté ocupado
            if validez == None:             # Si esta ocupado devuelve True, sino None
                return usuario
            print("Usuario inválido/Ya en uso")
        else: 
            print("¡El nombre de usuario ingresado es inválido!\n")

def validar_id(usuarios_datos, id):   #Valida que el ID utilizado no se repita
    coincidencias = [fila for fila in usuarios_datos if fila[4] == id]
    return len(coincidencias) == 0


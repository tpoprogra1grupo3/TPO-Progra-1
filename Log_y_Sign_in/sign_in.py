from funciones_utiles import buscar_nombre_usuario, titulo, limpiar_consola
import random
import re

def usuarios_de_base():   # Usuarios del sistema con su ID y rol 
    usuarios_datos = {
        'Juan': {
            'contraseña': 'Hola!',
            'ultimos_3_digitos': '836',
            'rol': 'admin',
            'id': 156836921,
            'mail': 'jrocca@uade.edu.ar'
        },
        'Elian': {
            'contraseña': '5555!',
            'ultimos_3_digitos': '856',
            'rol': 'admin',
            'id': 527856776,
            'mail': 'xxxx@uade.edu.ar'
        },
        'Facu': {
            'contraseña': '1234-',
            'ultimos_3_digitos': '185',
            'rol': 'socio',
            'id': 133185723,
            'mail': 'xxxx@uade.edu.ar'
        },
        'Iair007': {
            'contraseña': 'Messi@',
            'ultimos_3_digitos': '835',
            'rol': 'empleado',
            'id': 111835221,
            'mail': 'xxxx@uade.edu.ar'
        },
        'Esteban': {
            'contraseña': 'mentaaa#',
            'ultimos_3_digitos': '257',
            'rol': 'empleado',
            'id': 290257618,
            'mail': 'xxxx@uade.edu.ar'
        }
    }
    return usuarios_datos

def crear_usuario(usuarios_datos):
    usuario = crear_nombre_usuario(usuarios_datos)
    titulo(1)
    contraseña = crear_contraseña()
    titulo(1)
    mail = crear_mail(usuarios_datos)
    titulo(1)

    while True:
        dni_completo = input("Ingrese su DNI completo (9 dígitos): ")
        if dni_completo.isdigit() and len(dni_completo) == 9:
            ultimos_3_digitos = dni_completo[-3:]  # Se deja como string
            break
        else:
            print("DNI inválido. Asegúrese de ingresar exactamente 9 dígitos numéricos.")

    id = generar_id_usuario(usuarios_datos, ultimos_3_digitos)

    if len(usuarios_datos) == 0:
        permisos = "admin"
    else:
        permisos = "socio"

    # Se agrega al diccionario "Usuarios"
    usuarios_datos[usuario] = {
        'contraseña': contraseña,
        'ultimos_3_digitos': ultimos_3_digitos,
        'rol': permisos,
        'id': id,
        'mail': mail
    }

    limpiar_consola()

def crear_contraseña():
    longitud_min_contraseñas = 5
    print(f"\nRecuerde que su contraseña debe tener al menos:")
    print(f"\t-{longitud_min_contraseñas} dígitos")
    print(f"\t-Debe tener por lo menos 1 carácter especial")
    print(f"\t-No debe tener espacios vacíos (No se puede dejar huecos entre caracteres)")
    while True:
        contraseña = input("\nIngrese una contraseña: ")
        if not contraseña.isalnum(): 
            if len(contraseña) >= longitud_min_contraseñas:
                if " " not in contraseña:
                    return contraseña
        print("Contraseña inválida")

def generar_id_usuario(usuarios_datos, dni):
    while True:
        cadena_delantera = ''.join(str(random.randint(0, 9)) for _ in range(3))
        cadena_trasera = ''.join(str(random.randint(0, 9)) for _ in range(3))
        id = cadena_delantera + dni + cadena_trasera
        if validar_id(usuarios_datos, id):
            return id

def crear_nombre_usuario(usuarios_datos):
    while True:
        usuario = input("Ingrese el nombre de usuario que desea utilizar: ")
        if usuario.isalnum():
            if buscar_nombre_usuario(usuarios_datos, usuario) is None:
                return usuario
            print("Usuario inválido/Ya en uso")
        else:
            print("¡El nombre de usuario ingresado es inválido!\n")

def validar_id(usuarios_datos, id):
    for datos in usuarios_datos.values():
        if datos['id'] == int(id):
            return False
    return True

def crear_mail(usuarios_datos):
    while True:
        mail = input("Ingrese su e-mail: ")
        if re.search(r"\S+@\S+\.\S+", mail):
            for datos in usuarios_datos.values():
                if datos['mail'] == mail:
                    print("\nEl mail ingresado ya está en uso\n")
                    break
            else:
                return mail
        else:
            print("\nEl mail introducido es inválido\n")
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
            'mail': 'elianbineder@uade.edu.ar'
        },
        'Facu': {
            'contraseña': '1234-',
            'ultimos_3_digitos': '196',
            'rol': 'socio',
            'id': 133185723,
            'mail': 'fbueguez@uade.edu.ar'
        },
        'Iair007': {
            'contraseña': 'Messi@',
            'ultimos_3_digitos': '835',
            'rol': 'empleado',
            'id': 111835221,
            'mail': 'iair007@uade.edu.ar'
        },
        'Esteban': {
            'contraseña': 'mentaaa#',
            'ultimos_3_digitos': '257',
            'rol': 'empleado',
            'id': 290257618,
            'mail': 'juanesteban@uade.edu.ar'
        }
    }
    return usuarios_datos

def crear_empleado(usuarios_datos):         # REVISARRRRRRR
    usuario = crear_nombre_usuario(usuarios_datos)
    titulo(1)
    contraseña = crear_contraseña()
    titulo(1)
    mail = crear_mail(usuarios_datos)
    titulo(1)
    while True:
        dni_completo = input("Ingrese su DNI completo (Máx 10 caracteres)(-1 para volver al menu): ")
        if dni_completo==-1:
            return -1
        elif dni_completo.isdigit() and len(dni_completo) <=10 and len(dni_completo)>=3:
            dni_completo = dni_completo.zfill(10)  # Tendrá siempre 10 caracteres
            ultimos_3_digitos = dni_completo[-3:]  # Se deja como string
            break
        else:
            print("DNI inválido. Asegúrese de ingresar exactamente 9 dígitos numéricos.")

    id = generar_id_usuario(usuarios_datos, ultimos_3_digitos)

    permisos = "empleado"

    # Se agrega al diccionario "Usuarios"
    usuarios_datos[usuario] = {
        'contraseña': contraseña,
        'ultimos_3_digitos': ultimos_3_digitos,
        'rol': permisos,
        'id': id,
        'mail': mail
    }

    limpiar_consola()


def crear_socio(usuarios_datos):
    usuario = crear_nombre_usuario(usuarios_datos)
    if usuario == "Volver":
        return "Volver"
    titulo(1)
    contraseña = crear_contraseña()
    if contraseña == "Volver":
        return "Volver"
    titulo(1)
    mail = crear_mail(usuarios_datos)
    if mail == "Volver":
        return "Volver"
    titulo(1)

    while True:
        dni_completo = input("Ingrese su DNI completo (Máx 10 caracteres)(-1 para volver al menu): ")
        if dni_completo=="-1":
            return "Volver"
        elif dni_completo.isdigit() and len(dni_completo) <=10 and len(dni_completo)>=3:
            dni_completo = dni_completo.zfill(10)  # Tendrá siempre 10 caracteres
            ultimos_3_digitos = dni_completo[-3:]  # Se deja como string
            break
        else:
            print("DNI inválido. Asegúrese de ingresar exactamente 9 dígitos numéricos.")

    id = generar_id_usuario(usuarios_datos, ultimos_3_digitos)

    # if len(usuarios_datos) == 0:
    #     permisos = "admin"
    # else:
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
        contraseña = input("\nIngrese una contraseña (-1 Para volver al menú): ")
        if not contraseña.strip() == "-1":
            if not contraseña.isalnum():   
                if len(contraseña) >= longitud_min_contraseñas:
                    if " " not in contraseña:
                        return contraseña
            print("Contraseña inválida")
        else:
            return "Volver"

def generar_id_usuario(usuarios_datos, dni):
    while True:
        cadena_delantera = ''.join(str(random.randint(0, 9)) for _ in range(3)) 
        cadena_trasera = ''.join(str(random.randint(0, 9)) for _ in range(3))   
        id = cadena_delantera + dni + cadena_trasera
        if validar_id(usuarios_datos, id):  # Verifica que no sea el mismo que otro usuario
            return id 

def crear_nombre_usuario(usuarios_datos):
    while True:
        usuario = input("Ingrese el nombre que desea utilizar (0 para volver): ")
        if usuario.strip()=="0": # Evitamos 0 acompañado de espacios en blanco
            return "Volver" 
        elif usuario.isalnum():
            if buscar_nombre_usuario(usuarios_datos, usuario) is None:      # Verifica que no esté en uso
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
        mail = input("Ingrese su e-mail (-1 para volver): ")
        if mail.strip() == "-1":
            return "Volver"
        elif re.search(r"\S+@\S+\.\S+", mail):    # Verifica que sea formato de mail
            for datos in usuarios_datos.values():
                if datos['mail'] == mail:
                    print("\nEl mail ingresado ya está en uso\n")
                    break
            else:
                return mail
        else:
            print("\nEl mail introducido es inválido\n")

def mostrar_usuarios(usuarios_datos):
    limpiar_consola()
    print("======= LISTA DE USUARIOS =======")
    if len(usuarios_datos) == 0:
        print("No hay usuarios registrados.")
    else:
        for nombre, datos in usuarios_datos.items():
            print(f"Usuario: {nombre}")
            print(f"  Contraseña: {datos['contraseña']}")
            print(f"  Últimos 3 dígitos del DNI: {datos['ultimos_3_digitos']}")
            print(f"  Rol: {datos['rol']}")
            print(f"  ID: {datos['id']}")
            print(f"  Mail: {datos['mail']}")
            print("---------------------------------")

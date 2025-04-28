import os

def limpiar_consola(): # Vacía la consola
    os.system("cls")

def buscar_nombre_usuario(usuarios_datos, nombre_usuario):
    nombre_usuario = nombre_usuario.lower()   # Busca un nombre de usuario sin importar mayúsculas

    for nombre in usuarios_datos:
        if nombre.lower() == nombre_usuario:
            return nombre  # Devuelve el nombre exactamente como está en la base

    return None

def encontrar_id_usuario(usuarios_datos, nombre_usuario):
    nombre_usuario = nombre_usuario.lower()   

    for nombre in usuarios_datos:
        if nombre.lower() == nombre_usuario:
            id_del_usuario = usuarios_datos[nombre]["id"]
            return id_del_usuario  # Devuelve el id del usuario

def buscar_fila_libro(libros,nombre):
    nombre = nombre.lower()   

    for i in range(0,len(libros)):
        if libros[i][0].lower() == nombre:
            return i  # Devuelve el id del usuario


def titulo(opcion):
    if opcion==1:
        limpiar_consola()
        print(f"||{" Usted esta creando un Usuario ":=^60}||", end="\n\n")
    else:
        limpiar_consola()
        print(f"||{" Usted está Iniciando Sesión ":=^60}||", end="\n\n")

def cambiar_rol(usuario_datos):
    limpiar_consola()
    while True:
        usuario_ingresado = input("Ingrese el nombre de usuario de la cuenta que desea hacer empleado: ").strip()
        nombre_real = buscar_nombre_usuario(usuario_datos, usuario_ingresado)  # Usa la búsqueda case-insensitive

        if nombre_real is not None:
            if usuario_datos[nombre_real]['rol'] == "socio":
                usuario_datos[nombre_real]['rol'] = "empleado"
                print("\nLos cambios se han realizado correctamente.\n")
            else:
                print("\nEl usuario ingresado ya cuenta con permisos de empleado/administrador.\n")
            break
        else:
            print("\nNo se ha encontrado el usuario ingresado.\n")
            print("1. Volver a intentar")
            print("2. Volver al menú\n")
            while True:
                opcion = input("Ingrese la opción que desea utilizar: ").strip()
                if opcion in ("1", "2"):
                    if opcion == "2":
                        return
                    else:
                        break
                else:
                    print("La opción ingresada es inválida.")

def es_numero_flotante(valor):       # Verifica si es un string con un numero flotante positivo
    valor = valor.replace(',', '.')  # Permite usar coma o punto
    partes = valor.split('.')
    return (
        len(partes) == 1 and partes[0].isdigit() or
        len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit()
    )

def convertir_a_flotante(valor):    # Convierte string a float reemplazando , por .
    valor = valor.replace(',', '.')
    return float(valor)

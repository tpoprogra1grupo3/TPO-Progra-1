import os

def limpiar_consola(): # Vacía la consola
    os.system("cls")

def buscar_nombre_usuario(usuarios_datos,usuario): # Devuelve fila (int) en la que se encuentra el nombre de usuario, o None
    for fila in range(0,len(usuarios_datos)):   
        if usuario == usuarios_datos[fila][0]:  # Mira fila a fila si el usuario existe en alguna lista de la matriz
            return fila                         # En caso de existir, devuelve la fila del usuario
        elif fila == len(usuarios_datos)-1:     
            return None                         # Caso contrario devuelve None
        
def titulo(opcion):
    if opcion==1:
        limpiar_consola()
        print(f"||{" Usted esta creando un Usuario ":=^60}||", end="\n\n")
    else:
        limpiar_consola()
        print("Usted a Iniciado Sesion!!")

def cambiar_rol(usuario_datos):
    limpiar_consola()
    while True:
        usuario_a_cambiar = input("Ingrese el nombre de usuario de la cuenta que desea hacer empleado: ")
        if buscar_nombre_usuario(usuario_datos, usuario = usuario_a_cambiar) != None:
            fila = buscar_nombre_usuario(usuario_datos, usuario = usuario_a_cambiar)
            if usuario_datos[fila][3] == "socio":
                usuario_datos[fila][3] = "empleado"
                print("\nLos cambios se han realizado correctamente\n")
                input("Ingrese enter para continuar: ")
                break
            else:
                print("\nEl usuario ingresado ya cuenta con permisos de empleado/administrador\n")
                input("Ingrese enter para continuar: ") 
                break
        else:
            print("\nNo se ha encontrado el usuario ingresado\n")
            print("1. Volverlo a intentar")
            print("2. Volver al menú de su cuenta\n\n")
            while True:
                opcion = input("Ingrese la opción que desea utilizar: ")
                if opcion=="1" or opcion=="2":
                    opcion = int(opcion)
                    if opcion == 2: 
                        return 
                    else:
                        break
                else:
                    print("La opción ingresada es inválida")        

def buscar_libro(libros,libro,editorial):     # Devuelve la fila donde se encuentra o None
    nombre_libro = libro.lower()
    editorial = editorial.lower()
    for fila in range(0,len(libros)):
        if libros[fila][0].lower() == nombre_libro:
            if libros[fila][4].lower() == editorial:
                return fila   
    return None

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

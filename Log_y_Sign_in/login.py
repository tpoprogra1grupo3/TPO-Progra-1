from funciones_utiles import buscar_nombre_usuario,limpiar_consola
import re
from .sign_in import crear_contraseña,guardar_usuarios_datos


def iniciar_sesion(usuarios_datos):   # Loguea el usuario y devuelve nombre/ID para uso posterior
    bandera = True
    while bandera:
        
        usuario_ingresado = input("Ingrese su nombre de usuario (-1 para volver)(2 para recuperar la cuenta/cambiar contraseña): ").strip()     # Elimino los espacios accidentales
        if usuario_ingresado == "-1":
            return 0,"Volver",0     # Se esperan tres valores en la funcion anterior
        elif usuario_ingresado == "2":
            cambiar_contrasenia(usuarios_datos)
            return 0,"Volver",0
        elif usuario_ingresado.isalnum():
            nombre_real = buscar_nombre_usuario(usuarios_datos, usuario_ingresado)  # Verifica que exista el usuario
            if nombre_real is not None: 
                while bandera:
                    contraseña = input("Ingrese su contraseña (-1 para volver): ").strip()
                    if contraseña == "-1":
                        return 0,"Volver",0
                    elif contraseña != "":
                        if contraseña == usuarios_datos[nombre_real]['contraseña']: # Comprueba que la password sea correcta
                            rol = usuarios_datos[nombre_real]['rol']
                            id_usuario = usuarios_datos[nombre_real]['id']
                            return rol, nombre_real, id_usuario
                        else:
                            print("\nContraseña incorrecta\n")
                    else:
                        print("¡Debe ingresar una contraseña!")
            else:
                print("\nEse usuario no existe\n")
        else:
            print("¡Debe ingresar un usuario válido!")

def cambiar_contrasenia(usuarios_datos):
    while True:         # Valida el nombre
        usuario_ingresado = input("Ingrese su nombre de usuario o (-1 para cancelar): ")
        if usuario_ingresado.strip() == "-1":
            return "Volver"
        elif len(usuario_ingresado) == 0:
            print("No se han ingresado valores\n")
        else:
            usuario_ingresado = buscar_nombre_usuario(usuarios_datos, usuario_ingresado)
            if usuario_ingresado is not None:
                break
            else: 
                print("No existe un usuario con ese nombre de usuario\n")

    while True:         # Valida el dni
        try:
            dni_usuario_ingresado = input("\nIngrese los últimos tres dígitos de su dni (-1 para volver): ") 
            dni_usuario_ingresado = int(dni_usuario_ingresado.strip())

            if dni_usuario_ingresado == -1:             
                return "Volver"  
            elif len(str(dni_usuario_ingresado)) != 3:
                raise Exception("\nSe ingresaron más/menos de tres dígitos")        # Tipo de error generico, para que no se confunda con el ValueError forzado
            else:
                if str(dni_usuario_ingresado) == usuarios_datos[usuario_ingresado]["ultimos_3_digitos"]:
                    break
                else:
                    print("\nEl dni no coincide con el del usuario ingresado\n")
                
        except ValueError:
                print("\nNo se han ingresado dígitos")
        except Exception as err:
                print(f"\n{err}") 
        
    
    while True:         # Valida el mail
        mail = input("Ingrese el mail del usuario (-1 para volver): ")
        if mail.strip() == "-1":
            return "Volver"
        elif re.search(r"\S+@\S+\.\S+", mail):    # Verifica que sea formato de mail
            if mail == usuarios_datos[usuario_ingresado]["mail"]: 
                break
            else:
                print("\nEl mail es incorrecto\n")
        else:
            print("\nEl mail introducido es inválido\n")
    
    # A partir de aca, el usuario ya confirmo tener mail, dni y nombre de usuario
    limpiar_consola()
    print(f"||{" Usted esta creando una nueva contraseña ":=^60}||", end="\n\n")
    nueva_contrasenia = crear_contraseña()      # Se valida dentro de la función
    try:
        usuarios_datos[usuario_ingresado]["contraseña"] = nueva_contrasenia
        guardar_usuarios_datos(usuarios_datos)
        print("Se ha cambiado la contraseña correctamente\n")
    except:
        print("Ha ocurrido un error al guardar los datos\n")

    input("Presione ENTER para continuar...")
    return


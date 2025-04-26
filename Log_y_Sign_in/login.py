from funciones_utiles import buscar_nombre_usuario

def iniciar_sesion(usuarios_datos):
    bandera = True
    while bandera:
        usuario = input("Ingrese su nombre de usuario: ")
        if usuario.isalnum():
            existe_usuario = buscar_nombre_usuario(usuarios_datos, usuario)
            if existe_usuario is not None:
                while bandera:
                    contraseña = input("Ingrese su contraseña: ")
                    if contraseña.strip() != "":
                        if contraseña == usuarios_datos[usuario]['contraseña']:
                            return usuarios_datos[usuario]['rol']  # Devuelve el rol asociado al usuario
                        else:
                            print("\nContraseña incorrecta\n")
                    else:
                        print("¡Debe ingresar una contraseña!")
            else:
                print("\nEse usuario no existe\n")
        else:
            print("¡Debe ingresar un usuario!")
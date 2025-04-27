from funciones_utiles import buscar_nombre_usuario

def iniciar_sesion(usuarios_datos):
    bandera = True
    while bandera:
        usuario_ingresado = input("Ingrese su nombre de usuario: ").strip()
        if usuario_ingresado.isalnum():
            nombre_real = buscar_nombre_usuario(usuarios_datos, usuario_ingresado)
            if nombre_real is not None:
                while bandera:
                    contraseña = input("Ingrese su contraseña: ").strip()
                    if contraseña != "":
                        if contraseña == usuarios_datos[nombre_real]['contraseña']:
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
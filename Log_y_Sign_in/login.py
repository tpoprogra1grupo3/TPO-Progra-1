from funciones_utiles import buscar_nombre_usuario

def iniciar_sesion(usuarios_datos):   # Loguea el usuario y devuelve nombre/ID para uso posterior
    bandera = True
    while bandera:
        usuario_ingresado = input("Ingrese su nombre de usuario (-1 para volver): ").strip()     # Elimino los espacios accidentales
        if usuario_ingresado == "-1":
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
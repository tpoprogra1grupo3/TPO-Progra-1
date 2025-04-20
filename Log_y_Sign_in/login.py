from funciones_utiles import buscar_nombre_usuario

def iniciar_sesion(usuarios_datos):
    bandera = True
    while bandera:
        usuario = input("Ingrese su nombre de usuario: ")
        if usuario.isalnum() == True:
            fila = buscar_nombre_usuario(usuarios_datos,usuario) # Busca la lista de la matriz correspondiente al usuario
            if fila!=None:
                while bandera:
                    contraseña = input("Ingrese su contraseña: ")
                    if contraseña != " " or contraseña != "" or contraseña != "  " or contraseña != None:
                        if contraseña == usuarios_datos[fila][1]:    # Se válida que la contraseña ingresada sea la pertenenciente al usuario
                            return usuarios_datos[fila][3]          # Retorna el rol/rango del usuario
                        else:
                            print("\nContraseña incorrecta\n") 
                    else:
                        print("¡Debe ingresar una contraseña!")
            else: 
                print("\nEse usuario no existe\n")
        else: 
            print("¡Debe ingresar un usuario!")
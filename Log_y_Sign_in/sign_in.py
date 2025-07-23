from funciones_utiles import buscar_nombre_usuario, titulo, limpiar_consola
import random
import re
import json

def usuarios_de_base():   # Usuarios del sistema con su ID y rol 
    try:
        with open("Archivos_JSON/usuarios_datos.json","r",encoding="UTF-8") as archivo_usuarios:
            try:
                usuarios_datos = json.load(archivo_usuarios)
                return usuarios_datos

            except:
                print("Ha ocurrido un error al leer los datos de un usuario")
    except:
        print("Se ha producido un error al cargar los archivos de usuarios del programa")


def crear_usuario(usuarios_datos):
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
        if dni_completo.strip()=="-1":
            return "Volver"
        elif dni_completo.isdigit() and len(dni_completo) <=10 and len(dni_completo)>=3:
            dni_completo = dni_completo.zfill(10)  # Tendrá siempre 10 caracteres
            ultimos_3_digitos = dni_completo[-3:]  # Se deja como string
            break
        else:
            print("DNI inválido. Asegúrese de ingresar exactamente 9 dígitos numéricos.")

    id = generar_id_usuario(usuarios_datos, ultimos_3_digitos)

    # Selección de rol

    while True:
        print("\nSeleccione el rol del nuevo usuario (-1 para volver al menú):")
        print("1. Administrador")
        print("2. Socio")
        opcion = input("Ingrese 1 o 2: ")

        if opcion.strip() == "-1":
            return "Volver"
        elif opcion == "1":
            #Confirmacion Rol Admin
            master_key= "1234"
            intentos = 3
            while intentos > 0:
                clave_ingresada = input("Ingrese la clave para crear un Admin: ")
                if clave_ingresada == master_key:    # Confirmación adicional para creación de cuenta admin
                    permisos = "admin"
                    intentos = "Contraseña correcta"
                    break
                else:
                    intentos -= 1
                    print(f"Clave incorrecta. Intentos restantes: {intentos}")
                    if intentos == 0:
                        print("No se pudo verificar la clave. Cancelando creación de administrador.")
                        return -1

            if intentos == "Contraseña correcta":
                break

        elif opcion == "2":
            permisos = "socio"
            break

        else:
            print("Opción inválida. Intente de nuevo.")

    # Se agrega al diccionario "Usuarios"
    try:
        usuarios_datos[usuario] = {
            'contraseña': contraseña,
            'ultimos_3_digitos': ultimos_3_digitos,
            'rol': permisos,
            'id': int(id),
            'mail': mail
            }
        guardar_usuarios_datos(usuarios_datos) # Guardo cambios en el json
        print(f"Su id de usuario es {id}. RECUERDE ANOTAR ESTE DATO, PUEDE SER MUY IMPORTANTE PARA EL CORRECTO USO DE SU CUENTA")
    except:
        print("Ha ocurrido un error al crear el usuario.")

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
        mail = input("Crea su e-mail (-1 para volver): ")
        if mail.strip() == "-1":
            return "Volver"
        elif re.search(r"\S+@\S+\.\S+", mail):    # Verifica que sea formato de mail
            for datos in usuarios_datos.values():
                if datos['mail'] == mail:
                    print("\nEl mail ingresado ya está en uso\n")
                    break
            else:
                return mail.lower().strip()
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
            print(f"  Últimos 3 dígitos del DNI: {datos['ultimos_3_digitos']}")
            print(f"  Rol: {datos['rol']}")
            print(f"  ID: {datos['id']}")
            print(f"  Mail: {datos['mail']}")
            print("---------------------------------")

def guardar_usuarios_datos(usuarios_datos):
    try:
        with open("Archivos_JSON/usuarios_datos.json","w", encoding="UTF-8") as archivo_usuarios:
            try: 
                json.dump(usuarios_datos,archivo_usuarios,ensure_ascii=False) 
            except:
                print("No se han podido guardar los cambios en los archivos de programa")
    except:
        print("No se ha podido abrir el archivo")

def eliminar_usuarios_por_id(usuarios_datos,id_usuario_actual):
        id_usuario_actual = int(id_usuario_actual)
        while True:
            try:
                id_usuario = int(input("Ingrese el Id del usuario a eliminar(-1 para volver): ").strip())
                if id_usuario == -1:
                    return
                else:
                    break     
            except ValueError as er:
                print(f"Error: {er}. Igrese un numero de Id válido")
                continue            
        usuarios_a_eliminar = [nombre for nombre, datos in usuarios_datos.items() if datos.get("id") == id_usuario]  # itera nombre por cada dic(nombre/usuario) compara su id convertido a string y si existe lo agrega a la lista
            
        if usuarios_a_eliminar:  #si la lista no esta vacia
            for nombre in usuarios_a_eliminar:  #recorre los nombre con la lista anterior por tuplas(key,value)
                try:
                    del usuarios_datos[nombre]  
                    guardar_usuarios_datos(usuarios_datos)
                    print(f"El usuario {nombre} con el id {id_usuario} fue eliminado")
                    if id_usuario_actual == id_usuario:
                        return "volver_inicio"
                except:
                    print("No se pudo elimar el usuario")
        else: 
            print(f"Usuario con el id {id_usuario} no fue encontrado")       

def eliminar_mi_usuario(usuarios_datos, usuario_actual):
    confirmacion = input(f"¿Estás seguro que querés eliminar tu cuenta, {usuario_actual}? (s/n): ").lower()
    if confirmacion == "s":
        try:
            usuarios_datos.pop(usuario_actual, None)  # Se elimina y se verifica que no de errores
            guardar_usuarios_datos(usuarios_datos)
            print("Tu cuenta fue eliminada exitosamente.")
            return "volver_inicio"
        except:
            print("Ocurrió un error al eliminar tu cuenta.")
    else:
        print("Operación cancelada.")

def cambiar_mail(usuarios_datos, usuario_actual):
    confirmacion = input(f"¿Estás seguro que querés cambiar de mail, {usuario_actual}? (s/n): ").lower()
    if confirmacion == "s":
        nuevo_mail=crear_mail(usuarios_datos)
        if nuevo_mail == "Volver":
            print("Actualización cancelada.")
            return
        try:
            usuarios_datos[usuario_actual]["mail"] = nuevo_mail
            guardar_usuarios_datos(usuarios_datos)
            print("El mail ha sido actualizado correctamente.")
        except:
            print("Hubo un error al guardar el nuevo mail.")
            return "volver_inicio"
    else:
        print("Operación cancelada.")

def actualizar_usuario(usuarios_datos):
    limpiar_consola()
    print("== Actualización de usuario ==")

    print("\nLista de usuarios:")   # Se muestra los usuarios del sistema
    usuarios_lista = list(usuarios_datos.items())
    for i, (nombre, datos) in enumerate(usuarios_lista, start=1):
        print(f"{i}. {nombre} (ID: {datos['id']})")

    seleccion = input("\nIngrese el número del usuario a modificar (-1 para cancelar): ").strip()  # Selección del usuario a modificar
    if seleccion == "-1":
        return
    if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(usuarios_lista)):
        print("Selección inválida.")   # Se cancela en caso de ser inválido
        return

    seleccion = int(seleccion)
    usuario_encontrado = usuarios_lista[seleccion - 1][0]

    print(f"\nUsuario seleccionado: {usuario_encontrado}")
    print("1. Cambiar Mail")
    print("2. Cambiar Rol")
    print("3. Cambiar Contraseña")
    print("4. Cambiar Nombre de Usuario")
    print("5. Cancelar")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":   #Cambio de mail
        nuevo_mail = crear_mail(usuarios_datos)
        if nuevo_mail == "Volver":
            print("Operación cancelada.")
            return
        usuarios_datos[usuario_encontrado]["mail"] = nuevo_mail  

    elif opcion == "2": # Cambio de rol
        nuevo_rol = input("Ingrese el nuevo rol (admin / socio): ").strip().lower()
        if nuevo_rol in ("admin", "socio"):
            usuarios_datos[usuario_encontrado]["rol"] = nuevo_rol
        else:
            print("Rol inválido.")
            return

    elif opcion == "3": # Cambio de contraseña
        nueva_contraseña = crear_contraseña()
        if nueva_contraseña == "Volver":
            print("Operación cancelada.")
            return
        usuarios_datos[usuario_encontrado]["contraseña"] = nueva_contraseña

    elif opcion == "4": # Cambio de nombre de usuario
        nuevo_nombre = crear_nombre_usuario(usuarios_datos)
        if nuevo_nombre == "Volver":
            print("Operación cancelada.")
            return
        usuarios_datos[nuevo_nombre] = usuarios_datos.pop(usuario_encontrado)
        usuario_encontrado = nuevo_nombre

    elif opcion == "5": # Se cancela la modificación y vuelve al menu gestión de usuarios
        return

    else:
        print("Opción no válida.")
        return

    try:
        guardar_usuarios_datos(usuarios_datos)  # Guarda los cambios en archivo
        print("Los datos se actualizaron correctamente.")
    except:
        print("Error al guardar los datos actualizados.")

def eliminar_usuario(usuarios_datos, id_usuario_actual):
    limpiar_consola()
    print("== Eliminación de usuario ==")

    print("\nLista de usuarios:")     # Se muestra una lista de los usuarios del sistema
    usuarios_lista = list(usuarios_datos.items())
    for i, (nombre, datos) in enumerate(usuarios_lista, start=1):
        print(f"{i}. {nombre} (ID: {datos['id']})")

    seleccion = input("\nIngrese el número del usuario a eliminar (-1 para cancelar): ").strip() # Permite seleccionar el usuario a eliminar
    if seleccion == "-1":
        return
    if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(usuarios_lista)):
        print("Selección inválida.")    # Se cancela en caso de ser inválido
        return

    seleccion = int(seleccion)
    usuario_seleccionado, datos = usuarios_lista[seleccion - 1]

    confirmacion = input(f"¿Está seguro que desea eliminar a '{usuario_seleccionado}'? (s/n): ").lower()  # Confirmación de eliminación
    if confirmacion == "s":
        try:
            del usuarios_datos[usuario_seleccionado]
            guardar_usuarios_datos(usuarios_datos)
            print("Usuario eliminado exitosamente.")   # Usuario eliminado correctamente
            if datos["id"] == int(id_usuario_actual):
                print("\nSe ha eliminado el usuario actualmente en sesión. Cerrando sesión...")
                return "volver_inicio"
        except:
            print("Error al eliminar el usuario.")
    else:
        print("Operación cancelada.")
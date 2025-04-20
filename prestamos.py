from datetime import datetime, date, time, timedelta
from funciones_utiles import buscar_libro,buscar_nombre_usuario,limpiar_consola

def crud_prestamos():
    prestamos = [
    ["Facu",133185723,'El principito','L002',"Antoine de Saint-Exupéry",'Emecé',1300,date.today(),(date.today() + timedelta(weeks=1))],    
    ["Facu",133185723,'1984','L004',"George Orwell",'Destino',5400,date.today(),(date.today() + timedelta(weeks=3))]
    ]
    return prestamos

def crear_prestamos(usuarios_datos,libros,prestamos):
    while True:
        libro_a_alquilar = input("\n\nIngrese el nombre del libro a alquilar: ")
        editorial = input("\n\nIngrese el nombre de la editorial del libro a alquilar: ")
        if len(libro_a_alquilar)>0 and len(editorial)>0:                    # Se hacen las validaciones pertinentes
            fila_libro = buscar_libro(libros,libro_a_alquilar,editorial) 
            if fila_libro != None:
                if libros[fila_libro][3]>0:
                    while True:
                        semanas_a_alquilar = input("Ingrese la cantidad de semanas que desea alquilar el libro: ")
                        if semanas_a_alquilar.isnumeric() and semanas_a_alquilar!= "0":
                            semanas_a_alquilar = int(semanas_a_alquilar)
                            while True:
                                usuario_que_alquila = input("Ingrese el nombre del usuario que desea alquilar el libro (Respetar Mayúsculas): ")
                                if usuario_que_alquila.isalpha():
                                    fila_usuario = buscar_nombre_usuario(usuarios_datos,usuario_que_alquila)
                                    if fila_usuario != None:
                                        id_usuario_que_alquila = usuarios_datos[fila_usuario][4]    # Se establecen los datos del préstamo
                                        precio = (libros[fila_libro][5])*(semanas_a_alquilar/10)
                                        id_libro_a_alquilar = libros[fila_libro][1]
                                        autor_del_libro = libros[fila_libro][2]
                                        
                                        libro_a_alquilar = libro_a_alquilar.capitalize()
                                        editorial = editorial.capitalize()

                                        print("\n\nLos datos del préstamo son: ")
                                        print(f"{usuario_que_alquila}|{id_usuario_que_alquila}|{libro_a_alquilar}|{id_libro_a_alquilar}|{autor_del_libro}|{editorial}|${precio}")
                                        print(f"\nFecha de inicio: {date.today()}")
                                        print(f"Fecha de vencimiento: {date.today() + timedelta(weeks=semanas_a_alquilar)}\n")
                                        print("1. Confirmar los datos del préstamo")
                                        print("2. Cancelar el préstamo")
                                        while True:
                                            opcion = input("Ingrese la opción que desea utilizar: ")
                                            if opcion=="1":
                                                prestamos.append([usuario_que_alquila,id_usuario_que_alquila,libro_a_alquilar,id_libro_a_alquilar,autor_del_libro,editorial,precio,date.today(),date.today() + timedelta(weeks=semanas_a_alquilar)])
                                                libros[fila_libro][3] -= 1                             # Se quita una unidad
                                                limpiar_consola()
                                                print("Se ha creado el préstamo exitosamente\n")
                                                input("Pulse enter para continuar")
                                                return
                                            elif opcion=="2":
                                                return
                                            else:
                                                print("La opción ingresada es inválida")
                                    else:
                                        print("El usuario ingresado no existe")
                                else: 
                                    print("El usuario ingresado es inválido")
                        else:
                            print("La cantidad de semanas en inválida")
                else:
                    print("No hay más unidades disponibles de ese libro")    
            else:
                print("EL libro o editorial no existen")        
        else:
            print("El libro o editorial ingresados son inválido") 


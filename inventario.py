import os
def biblioteca():
    libros = [
    ['Cien años de soledad', 'L001', 'Gabriel García Márquez', 5, 'Sudamericana'],
    ['El principito', 'L002', 'Antoine de Saint-Exupéry', 10, 'Emecé'],
    ['Don Quijote de la Mancha', 'L003', 'Miguel de Cervantes', 3, 'Alfaguara'],
    ['1984', 'L004', 'George Orwell', 7, 'Destino'],
    ['Orgullo y prejuicio', 'L005', 'Jane Austen', 6, 'Alianza'],
    ['El señor de los anillos', 'L006', 'J.R.R. Tolkien', 2, 'Minotauro'],
    ['Harry Potter y la piedra filosofal', 'L007', 'J.K. Rowling', 9, 'Salamandra'],
    ['Matar un ruiseñor', 'L008', 'Harper Lee', 4, 'Debolsillo'],
    ['Crónica de una muerte anunciada', 'L009', 'Gabriel García Márquez', 8, 'Norma'],
    ['El código Da Vinci', 'L010', 'Dan Brown', 1, 'Planeta']
]
    return libros

def limpiar_consola(): # Vacía la consola
    os.system("cls")

def imprimir_libros(libros):     ##ESTA FUNCION MUESTRA LOS LIBROS COMO MATRIZ
    limpiar_consola()
    print(f"|{"Catálogo de Libros":-^60}|", end="\n\n")
    for libro in libros:
        print(f"Nombre: {libro[0]}")
        print(f"Código: {libro[1]}")
        print(f"Autor: {libro[2]}")
        print(f"Stock: {libro[3]}")
        print(f"Editorial: {libro[4]}")
        print("-" * 20)         ##SEPARACION ENTRE LOS LIBROS
    print("--- Fin del Catálogo ---")

def añadir_libro(libros):
    limpiar_consola()
    print(f"|{"Bienvenido a la carga de libros":-^60}|", end="\n\n")
    nuevo_nombre_libro=input("Ingrese el nombre del nuevo libro: ").lower()
    nuevo_autor_libro=input("Ingrese el autor: ").lower()
    nuevo_editorial_libro=input("Ingrese la editorial del libro: ").lower()
    
    existente=False           ##INTERRUPTOR PARA SABER SI EL LIBRO INGRESADO YA EXISTE

    for libro in libros:
        if (libro[0].lower()==nuevo_nombre_libro and
            libro[2].lower()==nuevo_autor_libro and     ##COMPARA TODOS LOS DATOS DE LOS LIBROS EN MINUS CON EL INGRESADO
            libro[4].lower()==nuevo_editorial_libro):
            libro[3]+=1                                 ##AÑADE UN EJEMPLAR MAS AL LIBRO QUE SE ENCONTRO
            print(f"El libro {nuevo_nombre_libro} ya existe y se añadió un ejemplar más!!")
            existente=True
            return      ##DEBE DEVOLVER ALGO

    if not existente:       ##DA ERROR CON existente==False
        nuevo_codigo_libro=input("Ingrese el nuevo codigo del libro: ")
        nuevo_libro=[nuevo_nombre_libro.title(), nuevo_codigo_libro, nuevo_autor_libro.title(), 1, nuevo_editorial_libro.title()]     ##LA PRIMERA LETRA DE CADA PALABRA EN MAYUS
        libros.append(nuevo_libro)
        print("El libro se ha cargado en la biblioteca con éxito!!")

def eliminar_libro(libros):     ##ESTA FUNCION SOLO LA UTILIZARA EL ADMINISTRADOR
    limpiar_consola()
    print(f"|{'Bienvenido a la eliminación de libros':-^60}|", end="\n\n")
    codigo_libro = input("Ingrese el nombre del libro a eliminar: ").lower()

    libro_encontrado = False
    for libro in libros:
        if libro[1].lower() == codigo_libro:
            libros.remove(libro)        ##ELIMINA EL LIBRO DE LA MATRIZ
            print(f"El libro '{libro[0]}' se ha eliminado de la biblioteca.")
            libro_encontrado = True
            return
    
    if not libro_encontrado:
        print("No se encontró el libro especificado.")

##MAIN_BIBLIOTECA
def main():
    print(f"|{"Bienvenido a la Biblioteca":-^60}|", end="\n\n")
    libros_biblioteca=biblioteca()
    opcion=input("¿Desea ver la biblioteca? si/no: ").lower()
    if opcion=="si":
        imprimir_libros(libros_biblioteca)
    elif opcion=="no":
        print("Bueno no hay problema")
    else:
        print("Opcion no valida")

    añadir = input("¿Desea añadir un libro a la biblioteca? (si/no): ").lower()
    if añadir == "si":
        añadir_libro(libros_biblioteca)
        ver_nueva_biblioteca = input("¿Desea ver la biblioteca actualizada? (si/no): ").lower()
        ver_nueva_biblioteca = ver_nueva_biblioteca.lower()
        if ver_nueva_biblioteca == "si":
            imprimir_libros(libros_biblioteca)
        else:
            return
    elif añadir == "no":
        print("No se añadirán libros.")
    else:
        print("Opción no válida.")


##Programa Principal
main()

##FALTA VALIDAR EL NUEVO CODIGO DEL LIBRO (QUE SEAN LETRAS Y NUMEROS)
##El MAIN DEBE SER MODIFICADO PARA ADMINISTRADOR Y CLIENTE
##CUIDADO CON EL ACENTO EN LOS NOMBRES DE LOS LIBROS
##LA FUNCION DE ELIMINAR NO SE LLAMA DENTRO DEL MENU 



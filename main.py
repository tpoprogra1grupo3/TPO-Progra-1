from modulo_libros import biblioteca
from menus import menu_inicio
from Log_y_Sign_in.sign_in import usuarios_de_base
from prestamos import cargar_prestamos, cambio_estado_inicio

def main():
    usuarios_datos = usuarios_de_base()  # Inicializo el DICCIONARIO de usuarios
    libros = biblioteca()
    prestamos = cargar_prestamos()
    cambio_estado_inicio(prestamos)  # Establece el estado de los mismos
    menu_inicio(usuarios_datos, libros, prestamos)

if __name__ == "__main__":
    main()  # Programa principal
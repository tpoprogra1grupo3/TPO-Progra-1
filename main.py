from inventario import biblioteca
from menus import menu_inicio
from Log_y_Sign_in.sign_in import usuarios_de_base
from prestamos import crud_prestamos

def main():
    usuarios_datos = usuarios_de_base()                 # Inicializo la MATRIZ de usuarios
    libros = biblioteca()
    prestamos = crud_prestamos()
    menu_inicio(usuarios_datos,libros,prestamos)



main()                                  # Programa Principal
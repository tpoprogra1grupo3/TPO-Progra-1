from inventario import biblioteca
from menus import menu_inicio

def main():
    usuarios_datos = []                 # Inicializo la MATRIZ de usuarios
    libros = biblioteca()
    menu_inicio(usuarios_datos,libros)



main()                                  # Programa Principal
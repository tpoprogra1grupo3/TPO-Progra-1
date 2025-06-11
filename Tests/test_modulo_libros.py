from modulo_libros import biblioteca,cargar_libros

def test_biblioteca_no_vacia():  #Testea que la biblioteca contenga elementos
    libros = cargar_libros()
    assert type(libros) is list
    assert len (libros) >= 1
    
def test_libro_individual(): #Testea que los libros se encuentren correctamente clasificados
    libros = cargar_libros()
    for libro in libros:
        assert type(libro) is list
        assert len (libro) == 5

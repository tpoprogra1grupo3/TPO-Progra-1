from modulo_libros import biblioteca

def test_biblioteca_no_vacia():  #Testea que la biblioteca contenga elementos
    libros = biblioteca()
    assert type(libros) is list
    assert len (libros) == 10
    
def test_primer_libro(): #Testea primer libro en la biblioteca
    libros = biblioteca()
    assert libros [0] ==  ['Cien años de soledad', 'L001', 'Gabriel García Márquez', 5, 'Sudamericana']

def test_libro_individual(): #Testea que los libros se encuentren correctamente clasificados
    libros = biblioteca()
    for libro in libros:
        assert type(libro) is list
        assert len (libro) == 5

def test_ultimo_libro(): #Testea ultimo libro en la biblioteca
    libros = biblioteca()
    assert libros [9] ==  ['El código Da Vinci', 'L010', 'Dan Brown', 1, 'Planeta']
from prestamos import crud_prestamos

def test_elementos_prestamo():
    prestamos = crud_prestamos()
    for prestamo in prestamos:
        assert len(prestamo) == 10  # Cantidad de elementos/categorias por prestamo
        assert type(prestamo) == tuple  # Cada prestamo es una tupla individual
        assert type(prestamos) == list  # Estan todas las tuplas en una lista 


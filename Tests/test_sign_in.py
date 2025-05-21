from Log_y_Sign_in.sign_in import usuarios_de_base

def test_usuarios_no_vacio():
    usuarios = usuarios_de_base()
    assert len(usuarios) >= 1   # Mínimo un usuario existente
    assert type(usuarios) == dict   # Los usuarios se encuentran en un diccionario, con diccionarios dentro

def test_elementos_usuarios():
    usuarios = usuarios_de_base()
    for usuario in usuarios:
        assert type(usuario) == str # Las keys de usuarios deben ser str (username)
        assert len(usuarios.get(usuario)) == 5  # Deben tener 5 valores para cada user
        assert type(usuarios.get(usuario)) == dict # El value de cada username es un diccionario



# Sistema de Gestión de Biblioteca

Aplicación de consola en Python para administrar una biblioteca: catálogo de libros, usuarios con roles y préstamos con control de vencimientos.

Trabajo Práctico Obligatorio de Programación I — Ingeniería en Informática, UADE.

**Stack:** Python 3 · archivos TXT y JSON para persistencia · tests automatizados

---

## Funcionalidades

**Acceso**
- Registro e inicio de sesión de usuarios.
- Cambio de contraseña.
- Dos roles con menús distintos: **administrador** y **socio**.

**Administrador**
- Catálogo: alta, baja, búsqueda y edición de libros. Al agregar un libro que ya existe, suma stock en vez de duplicarlo.
- Préstamos: crear, listar con filtros por estado, extender el vencimiento, registrar devoluciones y eliminar.
- Usuarios: listar, editar y dar de baja socios.

**Socio**
- Ver los libros disponibles y buscarlos por distintos criterios.
- Pedir un préstamo y consultar los propios.
- Gestionar su cuenta: ver su ID, cambiar el email y eliminar la cuenta.

## Cómo funcionan los préstamos

Cada préstamo tiene uno de tres estados:

| Estado | Cuándo |
|---|---|
| En curso | Todavía no llegó la fecha de vencimiento |
| Vencido | La fecha de vencimiento ya pasó |
| Devuelto | El libro se devolvió |

Los estados se recalculan automáticamente cada vez que arranca el programa, comparando la fecha de vencimiento con la fecha actual. Eliminar un préstamo devuelve el libro al stock, y editar un libro actualiza también los préstamos que lo referencian.

## Aspectos técnicos

- **Modularización:** cada responsabilidad vive en su propio módulo (`modulo_libros.py`, `prestamos.py`, `menus.py`, `Log_y_Sign_in/`).
- **Persistencia en archivos:** libros y préstamos se guardan en TXT, y los datos de usuarios en JSON.
- **Búsqueda con expresiones regulares:** los libros se buscan sin distinguir mayúsculas de minúsculas.
- **Recursividad:** se usa para leer los archivos de datos línea por línea.
- **Manejo de fechas:** con `datetime` y `timedelta`, para vencimientos y extensiones.
- **Manejo de errores:** `try/except` en la lectura y escritura de archivos y en la validación de entradas.
- **Estructuras de datos:** diccionarios, tuplas, conjuntos, listas por comprensión y funciones lambda.
- **Interfaz de consola:** tablas formateadas y colores por estado del préstamo.

## Estructura

```
├── main.py              # Punto de entrada
├── menus.py             # Menús por rol
├── modulo_libros.py     # Catálogo de libros
├── prestamos.py         # Préstamos y estados
├── funciones_utiles.py  # Utilidades compartidas
├── Log_y_Sign_in/       # Registro e inicio de sesión
├── Archivos_TXT/        # Datos de libros y préstamos
├── Archivos_JSON/       # Datos de usuarios
└── Tests/               # Tests automatizados
```

## Cómo ejecutarlo

Requiere Python 3.

```bash
git clone https://github.com/tpoprogra1grupo3/TPO-Progra-1.git
cd TPO-Progra-1
python main.py
```

La documentación completa del proyecto está en `Grupo 3 - Informe de Proyecto-1.pdf`.

---

**Equipo — Grupo 3:** Facundo Burguez · _(completar con los nombres del grupo)_

# ========================================================================================================== #
# Este proyecto esta documentado segun las especificaciones vistas en clase:
#   Descripcion:
#   Input y Output: Se omitiran ya que ninguna de las funciones en este archivo tienen Input ni Output)
# ========================================================================================================== #

from Entidades import Biblioteca

biblioteca = Biblioteca()

# ====================================================== #
# ==========  RF1 — Alta y gestion de libros  ========== #
# ====================================================== #

def interfaz_registrar_libro():
    #   Descripcion: Pide los datos al usuario por consola para registrar un libro
    print("--- Nuevo Libro ---")
    isbn = input("ISBN: ")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    stock = int(input("Stock: "))
    
    biblioteca.registrar_libro(isbn, titulo, autor, stock)


def interfaz_consultar_disponibilidad():
    #   Descripcion: Pide el ISBN e imprime si hay stock disponible o errores
    print("\n--- Consultar Disponibilidad ---")
    isbn = input("Ingrese el ISBN del libro: ")
    
    cantidad = biblioteca.consultar_disponibilidad(isbn)
    
    if cantidad == -1:
        print("El libro con ese ISBN no esta registrado en el catalogo.")
    elif cantidad == 0:
        print("No hay ejemplares disponibles para prestamo.")
    else:
        titulo = biblioteca.catalogo[isbn].titulo
        print(f"El libro '{titulo}' tiene {cantidad} ejemplares listos para prestamo.")


def interfaz_buscar_titulo():
    #   Descripcion: Pide un texto y muestra los libros que coincidan en el titulo
    print("\n--- Buscar por Titulo ---")
    termino = input("Escriba el titulo o parte de el: ")
    resultados = biblioteca.buscar_por_titulo(termino)
    
    if resultados:
        print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
        for libro in resultados:
            print(libro)
    else:
        print("No se encontraron libros con ese titulo.")


def interfaz_buscar_autor():
    #   Descripcion: Pide un texto y muestra los libros que coincidan en el autor
    print("\n--- Buscar por Autor ---")
    termino = input("Escriba el nombre del autor: ")
    resultados = biblioteca.buscar_por_autor(termino)
    
    if resultados:
        print(f"\nLibros de '{termino}':")
        for libro in resultados:
            print(libro)
    else:
        print("No se encontraron libros de ese autor.")

# ================================================== #
# ==========  RF2 — Registro de usuarios  ========== #
# ================================================== #

def interfaz_alta_usuario():
    #   Descripcion: Pide los datos para crear un usuario y maneja el exito o error
    print("\n--- Alta de Usuario ---")
    id_usuario = input("Ingrese el ID del usuario (debe ser unico): ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    
    exito = biblioteca.registrar_usuario(id_usuario, nombre, apellido)
    
    if exito:
        print(f"Usuario '{nombre} {apellido}' registrado con exito!")
    else:
        print("Error: Ya existe un usuario registrado con ese ID. Intente con otro.")

def interfaz_consultar_usuarios():
    #   Descripcion: Obtiene la lista de usuarios y los imprime en consola
    print("\n--- Lista de Usuarios Registrados ---")
    lista_usuarios = biblioteca.obtener_usuarios()
    
    if not lista_usuarios:
        print("Aun no hay usuarios registrados en el sistema.")
    else:
        for usuario in lista_usuarios:
            print(usuario)

# ====================================================== #
# ==========  RF3 — Prestamos y devoluciones  ========== #
# ====================================================== #

def interfaz_registrar_prestamo():
    print("\n--- Registrar Prestamo ---")
    isbn = input("ISBN del libro a prestar: ")
    id_usuario = input("ID del usuario que realiza el prestamo: ")
    
    if biblioteca.validar_disponibilidad(isbn):
        biblioteca.registrar_prestamo(isbn, id_usuario)
        print("Prestamo registrado exitosamente.")
    else:
        print("No se pudo registrar el prestamo ya que actualmente no hay ejemplares disponibles.")

def interfaz_registrar_devolucion():
    print("\n--- Registrar Devolucion ---")
    isbn = input("ISBN del libro a devolver: ")
    id_usuario = input("ID del usuario que realiza la devolucion: ")
    
    biblioteca.registrar_devolucion(isbn, id_usuario)
    print("Devolucion registrada exitosamente.")

def interfaz_libros_mas_prestados():
    print("\n--- Libros Mas Prestados ---")
    mas_prestados = biblioteca.libros_mas_prestados()
    
    if mas_prestados:
        print("Los libros mas prestados son:")
        for libro in mas_prestados:
            print(libro)
    else:
        print("No hay prestamos registrados.")
    

def interfaz_reporte_prestamos_activos():
    print("\n--- Reporte de Prestamos Activos ---")
    prestamos_activos = biblioteca.prestamos_activos()
    
    if prestamos_activos:
        print("Prestamos activos:")
        for isbn, id_usuario in prestamos_activos:
            libro = biblioteca.catalogo[isbn]
            usuario = biblioteca.usuarios[id_usuario]
            print(f"Libro: {libro.titulo} (ISBN: {isbn}) - Usuario: {usuario.nombre} (ID: {id_usuario})")
    else:
        print("No hay prestamos activos.")

def interfaz_consulta_libros_autor():
    print("\n--- Consulta de Libros por Autor ---")
    autor = input("Ingrese el nombre del autor: ")
    libros_autor = biblioteca.consulta_libros_autor(autor)
    
    if libros_autor:
        print(f"Libros de {autor}:")
        for libro in libros_autor:
            print(libro)
    else:
        print(f"No se encontraron libros de {autor}.")
   
#   Descripcion: Bucle infinito que mantiene la ejecucion del programa
#   Controla el flujo de navegacion entre los submenus del sistema
while True:
    print("""\nSelecciona el numero correspondiente a la opcion deseada [1-5]
    1) Alta y gestion de libros
    2) Registro de usuarios
    3) Prestamos y devoluciones
    4) Reportes y consultas
    5) Salir
    """)

    opc = input()

    if opc == "1":
        while True:
            print("""\nSelecciona el numero correspondiente a la opcion deseada [1-5]
            1) Registrar libro
            2) Consultar disponibilidad
            3) Buscar por titulo
            4) Buscar por autor
            5) Regresar
            """)

            opc2 = input()

            if opc2 == "1": interfaz_registrar_libro()
            elif opc2 == "2": interfaz_consultar_disponibilidad()
            elif opc2 == "3": interfaz_buscar_titulo()
            elif opc2 == "4": interfaz_buscar_autor()
            elif opc2 == "5": break
            else: print("Opcion no valida, intente de nuevo")
    
    elif opc == "2":
        while True:
            print("""\nSelecciona el numero correspondiente a la opcion deseada [1-3]
            1) Alta de usuario
            2) Consultar usuarios existentes
            3) Regresar
            """)

            opc2 = input()

            if opc2 == "1": interfaz_alta_usuario()
            elif opc2 == "2": interfaz_consultar_usuarios()
            elif opc2 == "3": break
            else: print("Opcion no valida, intente de nuevo")
    
    elif opc == "3":
        while True:
            print("""Selecciona el numero correspondiente a la opcion deseada [1-3]
            1) Registrar prestamo
            2) Registrar devolucion
            3) Regresar
            """)

            opc2 = input()

            if opc2 == "1": interfaz_registrar_prestamo()
            elif opc2 == "2": interfaz_registrar_devolucion()
            elif opc2 == "3": break
            else: print("Opcion no valida, intente de nuevo")
    
    elif opc == "4":
        while True:
            print("""Selecciona el numero correspondiente a la opcion deseada [1-4]
            1) Libros mas prestados
            2) Reporte de libros disponibles
            3) Reporte de prestamos activos
            4) Regresar
            """)

            opc2 = input()

            if opc2 == "1": interfaz_libros_mas_prestados()
            elif opc2 == "2": interfaz_reporte_prestamos_activos()
            elif opc2 == "3": interfaz_consulta_libros_autor()
            elif opc2 == "4": break
            else: print("Opcion no valida, intente de nuevo")

    
    elif opc == "5":
        print("Hasta pronto!")
        break

    else: print("Opcion no valida, intente de nuevo")
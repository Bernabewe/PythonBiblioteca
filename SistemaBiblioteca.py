from Entidades import Biblioteca

biblioteca = Biblioteca()

def interfaz_registrar_libro():
    print("--- Nuevo Libro ---")
    isbn = input("ISBN: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    stock = int(input("Stock: "))
    
    biblioteca.registrar_libro(isbn, titulo, autor, stock)


def interfaz_consultar_disponibilidad():
    print("\n--- Consultar Disponibilidad ---")
    isbn = input("Ingrese el ISBN del libro: ")
    
    cantidad = biblioteca.consultar_disponibilidad(isbn)
    
    if cantidad == -1:
        print("El libro con ese ISBN no está registrado en el catálogo.")
    elif cantidad == 0:
        print("No hay ejemplares disponibles para préstamo.")
    else:
        titulo = biblioteca.catalogo[isbn].titulo
        print(f"El libro '{titulo}' tiene {cantidad} ejemplares listos para préstamo.")


def interfaz_buscar_titulo():
    print("\n--- Buscar por Título ---")
    termino = input("Escriba el título o parte de él: ")
    resultados = biblioteca.buscar_por_titulo(termino)
    
    if resultados:
        print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
        for libro in resultados:
            print(libro)
    else:
        print("No se encontraron libros con ese título.")


def interfaz_buscar_autor():
    print("\n--- Buscar por Autor ---")
    termino = input("Escriba el nombre del autor: ")
    resultados = biblioteca.buscar_por_autor(termino)
    
    if resultados:
        print(f"\nLibros de '{termino}':")
        for libro in resultados:
            print(libro)
    else:
        print("No se encontraron libros de ese autor.")

def interfaz_alta_usuario():
    print("\n--- Alta de Usuario ---")
    id_usuario = input("Ingrese el ID del usuario (debe ser único): ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    
    # Llamamos al método y guardamos el resultado (True o False)
    exito = biblioteca.registrar_usuario(id_usuario, nombre, apellido)
    
    if exito:
        print(f"¡Usuario '{nombre} {apellido}' registrado con éxito!")
    else:
        print("Error: Ya existe un usuario registrado con ese ID. Intente con otro.")

def interfaz_consultar_usuarios():
    print("\n--- Lista de Usuarios Registrados ---")
    lista_usuarios = biblioteca.obtener_usuarios()
    
    # Validamos si el diccionario de usuarios está vacío
    if not lista_usuarios:
        print("Aún no hay usuarios registrados en el sistema.")
    else:
        # Si hay usuarios, los imprimimos uno por uno
        for usuario in lista_usuarios:
            print(usuario) # Llama automáticamente al __str__ de la clase Usuario

def interfaz_registrar_prestamo():
    print("\n--- Registrar Préstamo ---")
    isbn = input("ISBN del libro a prestar: ")
    id_usuario = input("ID del usuario que realiza el préstamo: ")
    
    if biblioteca.validar_disponibilidad(isbn):
        biblioteca.registrar_prestamo(isbn, id_usuario)
        print("Préstamo registrado exitosamente.")
    else:
        print("No se pudo registrar el préstamo ya que actualmente no hay ejemplares disponibles.")

def interfaz_registrar_devolucion():
    print("\n--- Registrar Devolución ---")
    isbn = input("ISBN del libro a devolver: ")
    id_usuario = input("ID del usuario que realiza la devolución: ")
    
    biblioteca.registrar_devolucion(isbn, id_usuario)
    print("Devolución registrada exitosamente.")

def interfaz_libros_mas_prestados():
    print("\n--- Libros Más Prestados ---")
    mas_prestados = biblioteca.libros_mas_prestados()
    
    if mas_prestados:
        print("Los libros más prestados son:")
        for libro in mas_prestados:
            print(libro)
    else:
        print("No hay préstamos registrados.")
    

def interfaz_reporte_prestamos_activos():
    print("\n--- Reporte de Préstamos Activos ---")
    prestamos_activos = biblioteca.prestamos_activos()
    
    if prestamos_activos:
        print("Préstamos activos:")
        for isbn, id_usuario in prestamos_activos:
            libro = biblioteca.catalogo[isbn]
            usuario = biblioteca.usuarios[id_usuario]
            print(f"Libro: {libro.titulo} (ISBN: {isbn}) - Usuario: {usuario.nombre} (ID: {id_usuario})")
    else:
        print("No hay préstamos activos.")

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
   

while True:
    print("""\nSelecciona el número correspondiente a la opción deseada [1-5]
    1) Alta y gestión de libros
    2) Registro de usuarios
    3) Préstamos y devoluciones
    4) Reportes y consultas
    5) Salir
    """)

    opc = input()

    if opc == "1":
        while True:
            print("""\nSelecciona el número correspondiente a la opción deseada [1-5]
            1) Registrar libro
            2) Consultar disponibilidad
            3) Buscar por título
            4) Buscar por autor
            5) Regresar
            """)

            opc2 = input()

            if opc2 == "1": interfaz_registrar_libro()
            elif opc2 == "2": interfaz_consultar_disponibilidad()
            elif opc2 == "3": interfaz_buscar_titulo()
            elif opc2 == "4": interfaz_buscar_autor()
            elif opc2 == "5": break
            else: print("Opcion no válida, intente de nuevo")
    
    elif opc == "2":
        while True:
            print("""\nSelecciona el número correspondiente a la opción deseada [1-3]
            1) Alta de usuario
            2) Consultar usuarios existentes
            3) Regresar
            """)

            opc2 = input()

            if opc2 == "1": interfaz_alta_usuario()
            elif opc2 == "2": interfaz_consultar_usuarios()
            elif opc2 == "3": break
            else: print("Opcion no válida, intente de nuevo")
    
    elif opc == "3":
        while True:
            print("""Selecciona el número correspondiente a la opción deseada [1-3]
            1) Registrar préstamo
            2) Registrar devolución
            3) Regresar
            """)

            opc2 = input()

            if opc2 == "1": interfaz_registrar_prestamo()
            elif opc2 == "2": interfaz_registrar_devolucion()
            elif opc2 == "3": break
            else: print("Opcion no válida, intente de nuevo")
    
    elif opc == "4":
        while True:
            print("""Selecciona el número correspondiente a la opción deseada [1-4]
            1) Libros más prestados
            2) Reporte de libros disponibles
            3) Reporte de préstamos activos
            4) Regresar
            """)

            opc2 = input()

            if opc2 == "1": interfaz_libros_mas_prestados()
            elif opc2 == "2": interfaz_reporte_prestamos_activos()
            elif opc2 == "3": interfaz_consulta_libros_autor()
            elif opc2 == "4": break
            else: print("Opcion no válida, intente de nuevo")

    
    elif opc == "5":
        print("¡Hasta pronto!")
        break

    else: print("Opcion no válida, intente de nuevo")
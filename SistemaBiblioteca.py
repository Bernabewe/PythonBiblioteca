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


while True:
    print("""Selecciona el número correspondiente a la opción deseada [1-5]
    1) Alta y gestión de libros
    2) Registro de usuarios
    3) Préstamos y devoluciones
    4) Reportes y consultas
    5) Salir
    """)

    opc = input()

    if opc == "1":
        while True:
            print("""Selecciona el número correspondiente a la opción deseada [1-5]
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
            print("""Selecciona el número correspondiente a la opción deseada [1-3]
            1) Alta de usuario
            2) Consultar usuarios existentes
            3) Regresar
            """)

            opc2 = input()

            if opc2 == "1": altaUsuario()
            elif opc2 == "2": ConsultarUsuarios()
            elif opc2 == "3": break
            else: print("Opcion no válida, intente de nuevo")
    
    elif opc == "5":
        print("¡Hasta pronto!")
        break

    else: print("Opcion no válida, intente de nuevo")
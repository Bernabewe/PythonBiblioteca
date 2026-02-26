# ===================================================================================== #
# Este proyecto esta documentado segun las especificaciones vistas en clase:
#   Descripcion:
#   Input:
#   Output:
# ===================================================================================== #

class Usuario:
    #   Descripcion: Molde para crear los usuarios de la biblioteca
    #   Input: id_usuario (string), nombre (string), apellido (string)
    #   Output: Objeto tipo Usuario
    def __init__(self, id_usuario, nombre, apellido):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.prestamos_actuales = []
    
    #   Descripcion: Agrega el ISBN de un libro a la lista personal del usuario
    #   Input: isbn (string)
    #   Output: Ninguno
    def agregarPrestamo(self, isbn):
        self.prestamos_actuales.append(isbn)

    def __str__(self):
        return f"\n[ID: {self.id_usuario}] {self.nombre} {self.apellido} - Libros en mano: {len(self.prestamos_actuales)}"


class Libro:
    #   Descripcion: Molde para crear los libros del catalogo
    #   Input: isbn (string), titulo (string), autor (string), stock (int)
    #   Output: Objeto tipo Libro
    def __init__(self, isbn, titulo, autor, stock):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_totales = stock
        self.ejemplares_disponibles = stock
        self.veces_prestado = 0

    def __str__(self):
        return f"\n[{self.isbn}] {self.titulo} - {self.autor} (Disponibles: {self.ejemplares_disponibles})"
    

class Biblioteca:
    #   Descripcion: Clase principal que gestiona las colecciones y la logica del sistema
    #   Input: Ninguno
    #   Output: Objeto tipo Biblioteca con diccionarios y listas vacias
    def __init__(self):
        self.catalogo = {} # Diccionario
        self.usuarios = {} # Diccionario
        self.prestamos = [] # Lista de tuplas
    
    # ====================================================== #
    # ==========  RF1 — Alta y gestión de libros  ========== #
    # ====================================================== #

    def registrar_libro(self, isbn, titulo, autor, stock):
        #   Descripcion: Crea un libro y lo guarda en el diccionario catalogo
        #   Input: isbn (string), titulo (string), autor (string), stock (int)
        #   Output: Imprime el objeto libro en consola
        libro_nuevo = Libro(isbn, titulo, autor, stock)
        self.catalogo[isbn] = libro_nuevo
        print(libro_nuevo)
    
    def consultar_disponibilidad(self, isbn):
        #   Descripcion: Busca un libro por su ISBN para verificar su stock
        #   Input: isbn (string)
        #   Output: Entero con los ejemplares disponibles, o -1 si no existe
        libro = self.catalogo.get(isbn)
        if libro: return libro.ejemplares_disponibles
        else: return -1

    def buscar_por_titulo(self, titulo_buscar):
        #   DescripciOn: Busca coincidencias parciales de un titulo en el catalogo
        #   Input: titulo_buscar (string)
        #   Output: Lista de objetos Libro que coinciden de alguna manera con el input
        encontrados = []
        for libro in self.catalogo.values():
            if titulo_buscar.lower() in libro.titulo.lower():
                encontrados.append(libro)
        return encontrados

    def buscar_por_autor(self, autor_buscar):
        #   Descripcion: Busca coincidencias parciales de un autor en el catalogo
        #   Input: autor_buscar (string)
        #   Output: Lista de objetos Libro que coinciden
        encontrados = []
        for libro in self.catalogo.values():
            if autor_buscar.lower() in libro.autor.lower():
                encontrados.append(libro)
        return encontrados

    # ================================================== #
    # ==========  RF2 — Registro de usuarios  ========== #
    # ================================================== #

    def registrar_usuario(self, id_usuario, nombre, apellido):
        #   Descripcion: Registra un usuario nuevo validando que el ID sea unico
        #   Input: id_usuario (string), nombre (string), apellido (string)
        #   Output: Booleano (True si se inserto, False si el ID ya existe)
        if id_usuario in self.usuarios:
            return False
        
        nuevo_usuario = Usuario(id_usuario, nombre, apellido)
        self.usuarios[id_usuario] = nuevo_usuario
        return True

    def obtener_usuarios(self):
        #   Descripcion: Recupera todos los usuarios registrados
        #   Input: Ninguno
        #   Output: Coleccion con los objetos Usuario
        return self.usuarios.values()
    
    # ====================================================== #
    # ==========  RF3 — Préstamos y devoluciones  ========== #
    # ====================================================== #

    def registrar_prestamo(self, isbn, id_usuario):

        #   Descripcion: Registra un préstamo actualizando el libro, el usuario y la lista de préstamos
        #   Input: isbn (string), id_usuario (string)
        if isbn not in self.catalogo:
            return False, "El ISBN ingresado no existe en el catalogo."

        if id_usuario not in self.usuarios:
            return False, "El usuario no existe en el sistema."

        libro = self.catalogo[isbn]
        usuario = self.usuarios[id_usuario]

        if libro.ejemplares_disponibles <= 0:
            return False, "No hay ejemplares disponibles para este libro."

        if isbn in usuario.prestamos_actuales:
            return False, "No se permite prestar el mismo libro dos veces al mismo usuario."

        if len(usuario.prestamos_actuales) >= 3:
            return False, "El usuario ya alcanzo el limite de 3 prestamos activos."
        
        # Actualizar el libro
        libro.ejemplares_disponibles -= 1
        libro.veces_prestado += 1
        
        # Actualizar el usuario
        usuario.agregarPrestamo(isbn)
        
        # Registrar el préstamo
        self.prestamos.append((isbn, id_usuario))
        return True, "Prestamo registrado exitosamente."
    
    def validar_disponibilidad(self, isbn):
        #   Descripcion: Valida si un libro está disponible para préstamo
        #   Input: isbn (string)
        #   Output: Booleano (True si está disponible, False si no lo está)

        libro = self.catalogo.get(isbn)
        if libro and libro.ejemplares_disponibles > 0:
            return True
        return False
    
    def registrar_devolucion(self, isbn, id_usuario):
        #   Descripcion: Registra una devolución actualizando el libro, el usuario y la lista de préstamos
        #   Input: isbn (string), id_usuario (string)  
        libro = self.catalogo[isbn]
        usuario = self.usuarios[id_usuario]
        
        # Actualizar el libro
        libro.ejemplares_disponibles += 1
        
        # Actualizar el usuario
        if isbn in usuario.prestamos_actuales:
            usuario.prestamos_actuales.remove(isbn)
        
    # ====================================================== #
    # ==========  RF4 — Consultas y reportes  ========== #
    # ====================================================== #  
  

    def libros_mas_prestados(self):
        
        # Retorna una lista de los 3 libros más prestados usando diccionario de frecuencias
        frecuencias = {}
        # Contar cuántas veces se ha prestado cada libro
        for isbn, _ in self.prestamos:
            frecuencias[isbn] = frecuencias.get(isbn, 0) + 1
        # Ordenar los ISBN por frecuencia y obtener los 3 más prestados
        top_isbn = sorted(frecuencias, key=frecuencias.get, reverse=True)[:3]
        return [self.catalogo[isbn] for isbn in top_isbn if isbn in self.catalogo]
    
    def prestamos_activos(self):
        # Retorna una lista de tuplas con los libros actualmente prestados y los usuarios que los tienen
        activos = []
        for isbn, id_usuario in self.prestamos:
            libro = self.catalogo[isbn]
            usuario = self.usuarios[id_usuario]
            if isbn in usuario.prestamos_actuales:
                activos.append((libro, usuario))
        return activos
    
    def consulta_libros_autor(self, autor):
        #  Descripcion: Consulta los libros de un autor específico
        #  Input: autor (string)
        return self.buscar_por_autor(autor)

    

# ===================================================================================== #
# Este proyecto esta documentado segun las especificaciones vistas en clase:
#   Descripcion:
#   Input:
#   Output:
# ===================================================================================== #

from datetime import datetime


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
        self.prestamos_activos = [] # Lista de tuplas vigentes
        self.prestamos_historicos = [] # Lista de tuplas (historial)
    
    # ====================================================== #
    # ==========  RF1 — Alta y gestion de libros  ========== #
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
    # ==========  RF3 — Prestamos y devoluciones  ========== #
    # ====================================================== #

    def registrar_prestamo(self, isbn, id_usuario):
        # Obtenemos la fecha actual y le damos formato DIA/MES/AÑO
        # Esto si se busco en internet
        fecha_hoy = datetime.now().strftime("%d/%m/%Y")
        
        libro = self.catalogo[isbn]
        usuario = self.usuarios[id_usuario]
        
        libro.ejemplares_disponibles -= 1
        libro.veces_prestado += 1
        
        usuario.agregarPrestamo(isbn)
        
        self.prestamos_historicos.append((isbn, id_usuario, fecha_hoy))
        self.prestamos_activos.append((isbn, id_usuario, fecha_hoy))

    def registrar_devolucion(self, isbn, id_usuario):
        libro = self.catalogo.get(isbn)
        usuario = self.usuarios.get(id_usuario)
        
        if not libro or not usuario: return False

        libro.ejemplares_disponibles += 1

        if isbn in usuario.prestamos_actuales:
            usuario.prestamos_actuales.remove(isbn)
    
        for t in self.prestamos_activos:
            if t[0] == isbn and t[1] == id_usuario:
                self.prestamos_activos.remove(t)
                return True
        return False

    def obtener_top_libros(self):
        conteo = {}
        
        for registro in self.prestamos_historicos:
            isbn = registro[0]
            if isbn in conteo:
                conteo[isbn] += 1
            else:
                conteo[isbn] = 1
                
        top_3_libros = []
        
        for i in range(3):
            max_v = -1
            isbn_mayor = None
            
            for isbn, valor in conteo.items():
                if valor > max_v:
                    max_v = valor
                    isbn_mayor = isbn
            
            if isbn_mayor:
                top_3_libros.append(self.catalogo[isbn_mayor])
                conteo[isbn_mayor] = -1
                
        return top_3_libros

    def consulta_prestamos_activos(self):
        return self.prestamos_activos
    
    # ====================================================== #
    # =============  RF5 — Reglas del negocio ============== #
    # ====================================================== #

    def validar_posibilidad_prestamo(self, isbn, id_usuario):
        libro = self.catalogo.get(isbn)
        if not libro:
            return "Error: El ISBN no existe en el catalogo."
        
        usuario = self.usuarios.get(id_usuario)
        if not usuario:
            return "Error: El ID de usuario no esta registrado."
        
        if libro.ejemplares_disponibles <= 0:
            return "Error: No hay ejemplares disponibles de este libro."
        
        if len(usuario.prestamos_actuales) >= 3:
            return "Error: El usuario ya tiene el limite de 3 prestamos activos."
        
        if isbn in usuario.prestamos_actuales:
            return "Error: El usuario ya cuenta con un ejemplar de este mismo libro."
        
        return True

    

class Usuario:
    def __init__(self, id_usuario, nombre, apellido):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.prestamos_actuales = []
    
    def agregarPrestamo(self, isbn):
        self.prestamos_actuales.append(isbn)

    def __str__(self):
        return f"\n[ID: {self.id_usuario}] {self.nombre} {self.apellido} - Libros en mano: {len(self.prestamos_actuales)}"


class Libro:
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
    def __init__(self):
        # Diccionario: { isbn: objeto_libro }
        self.catalogo = {}
        # Diccionario: { id_usuario: objeto_usuario }
        self.usuarios = {}
        # Lista de tuplas: [ (isbn, id_user, fecha), ... ]
        self.prestamos = []
    
    def registrar_libro(self, isbn, titulo, autor, stock):
        libro_nuevo = Libro(isbn, titulo, autor, stock)
        self.catalogo[isbn] = libro_nuevo
        print(libro_nuevo)
    
    def consultar_disponibilidad(self, isbn):
        libro = self.catalogo.get(isbn)
        if libro: return libro.ejemplares_disponibles
        else: return -1

    def buscar_por_titulo(self, titulo_buscar):
        encontrados = []
        for libro in self.catalogo.values():
            if titulo_buscar.lower() in libro.titulo.lower():
                encontrados.append(libro)
        return encontrados

    def buscar_por_autor(self, autor_buscar):
        encontrados = []
        for libro in self.catalogo.values():
            if autor_buscar.lower() in libro.autor.lower():
                encontrados.append(libro)
        return encontrados

    def registrar_usuario(self, id_usuario, nombre, apellido):
        if id_usuario in self.usuarios:
            return False
        
        nuevo_usuario = Usuario(id_usuario, nombre, apellido)
        self.usuarios[id_usuario] = nuevo_usuario
        return True

    def obtener_usuarios(self):
        return self.usuarios.values()
    
    def registrar_prestamo(self, isbn, id_usuario):
        libro = self.catalogo[isbn]
        usuario = self.usuarios[id_usuario]
        
        # Actualizar el libro
        libro.ejemplares_disponibles -= 1
        libro.veces_prestado += 1
        
        # Actualizar el usuario
        usuario.agregarPrestamo(isbn)
        
        # Registrar el préstamo
        self.prestamos.append((isbn, id_usuario))
    
    def validar_disponibilidad(self, isbn):
        libro = self.catalogo.get(isbn)
        if libro and libro.ejemplares_disponibles > 0:
            return True
        return False
    
    def registrar_devolucion(self, isbn, id_usuario):
        libro = self.catalogo[isbn]
        usuario = self.usuarios[id_usuario]
        
        # Actualizar el libro
        libro.ejemplares_disponibles += 1
        
        # Actualizar el usuario
        if isbn in usuario.prestamos_actuales:
            usuario.prestamos_actuales.remove(isbn)
        
    
  
    def libros_mas_prestados(self):
        libros = self.catalogo.values().split()
        frecuencia_dict = {}
        for libro in libros:
            frecuencia_dict[libro.titulo] = frecuencia_dict.get(libro.titulo, 0) + libro.veces_prestado
    
    
    def prestamos_activos(self):
        # Retorna una lista de préstamos que aún no han sido devueltos
        activos = []
        for isbn, id_usuario in self.prestamos:
            libro = self.catalogo[isbn]
            usuario = self.usuarios[id_usuario]
            if isbn in usuario.prestamos_actuales:
                activos.append((libro, usuario))
        return activos
    
    def consulta_libros_autor(self, autor):
        return self.buscar_por_autor(autor)

    

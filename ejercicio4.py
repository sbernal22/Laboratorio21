class Libro:
    def __init__ (self, titulo, autor, año, disponible):
        self.titulo=titulo
        self.autor=autor
        self.año=año
        self.disponible=disponible
    def prestar(self):
        if self.disponible:
            print("Libro prestado con exito")
            self.disponible=False
        else:
            print("El libro no esta disponible")
    def devolver(self):
        print("Libro devuelto")
        self.disponible=True

class LibroDigital(Libro):
    def __init__(self,titulo, autor, año, disponible, formato, tamañoMB):
        super(titulo, autor, año, disponible)
        self.formato=formato
        self.tamañoMB=tamañoMB
    def prestar(self):
        print("Libro prestado")

class Biblioteca:
    def __init__(self):
        self.listaLibros=[]
    def agregar_libro(self, Libro):
        self.listaLibros.append(Libro)
    def listar_libros(self):
        lista=[]
        for libro in self.listaLibros:
            lista.append(f"{libro.titulo}, {libro.disponible}")
        return lista
    def buscar_por_autor(self, autor):
        for libro in self.listaLibros:
            if libro.autor==autor:
                return libro
        return None
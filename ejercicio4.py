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
    def __init__(self, titulo, autor, año, disponible, formato, tamañoMB):
        super().__init__(titulo, autor, año, disponible)
        self.formato = formato
        self.tamañoMB = tamañoMB
    def prestar(self):
        print("Libro descargado con exito")

class Biblioteca:
    def __init__(self):
        self.listaLibros=[]
    def agregar_libro(self, libro):
        self.listaLibros.append(libro)
    def listar_libros(self):
        for libro in self.listaLibros:
            print(f"{libro.titulo}: {libro.disponible}")
    def buscar_por_autor(self, autor):
        for libro in self.listaLibros:
            if libro.autor.lower()==autor.lower():
                print(f"{libro.autor}: {libro.titulo}")
    def prestar_libro(self, titulo):
        for libro in self.listaLibros:
            if libro.titulo.lower() == titulo.lower():
                libro.prestar()

biblioteca=Biblioteca()
libro1 = Libro("Libro1", "Autor1", 1967, True)
libro2 = Libro("Libro2", "Autor2", 1605, True)
libro3 = Libro("Libro3", "Autor3", 1949, True)
libroD1 = LibroDigital("Libro4", "Autor4", 2020, True, "PDF", 5.2)
libroD2 = LibroDigital("Libro5", "Autor5", 2008, True, "EPUB", 3.8)
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libroD1)
biblioteca.agregar_libro(libroD2)

biblioteca.listar_libros()

biblioteca.prestar_libro("Libro3")

for i in range(5):
    biblioteca.prestar_libro("Libro4")

biblioteca.prestar_libro("Libro3")

biblioteca.buscar_por_autor("Autor3")
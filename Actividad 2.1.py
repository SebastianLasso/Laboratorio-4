class Biblioteca:

    def _init_(self):
        self.libros = []  # Lista de libros (estado interno)

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro}' agregado a la biblioteca.")

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro '{libro}' eliminado de la biblioteca.")
        else:
            print(f"Libro '{libro}' no encontrado.")

    def mostrar_libros(self):
        if self.libros:
            print("Libros en la biblioteca:", ", ".join(self.libros))
        else:
            print("La biblioteca está vacía.")
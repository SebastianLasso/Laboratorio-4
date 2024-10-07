class Album:
    def __init__(self):
        self.fotos = [] # Lista de fotos

    def agregar_fotos(self, foto):
        self.fotos.append(foto)
        print(f"Foto '{foto}' agregando al album.")

    def eliminar_foto(self, foto):
        if foto in self.fotos:
            self.fotos.remove(foto)
            print(f"Foto '{foto}' eliminada del album.")
        else:
            print(f"Foto '{foto}' no encontrada.")

    def mostrar_fotos(self):
        if self.fotos:
            print("Fotos en el album:", ", ".join(self.fotos))
        else:
            print("El album esta vacio.")
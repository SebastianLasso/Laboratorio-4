class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.estado = "despierto" # Estado inicial

        def dormir(self):
            self.estado = "durmiendo"

        def despertar(self):
            self.estado = "despierto"

        def mostrar_estado(self):
            print(f"{self.nombre} tiene {self.edad} años y esta {self.estado}.")
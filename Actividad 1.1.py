class Cafetera:

    def _init_(self, capacidad):
        self.capacidad = capacidad  # Capacidad máxima de la cafetera
        self._nivel_actual = 0      # Estado interno (nivel de café)

    def llenar(self):
        self._nivel_actual = self.capacidad
        print("La cafetera ha sido llenada.")

    def servir_taza(self):
        if self._nivel_actual > 0:
            self._nivel_actual -= 1
            print("Se ha servido una taza de café.")
        else:
            print("No hay café. Llena la cafetera.")

    def mostrar_nivel(self):
        print(f"Nivel actual de café: {self._nivel_actual} tazas.")
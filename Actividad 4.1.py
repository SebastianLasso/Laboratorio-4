class Temporizador:
    def __init__(self, tiempo_inicial):
        self.tiempo_restante = tiempo_inicial # Tiempo en segundos

    def iniciar(self):
        print(f"Temporizador iniciado con {self.tiempo_restante} segundos.")

    def pausar(self):
        print(f"Temporizador pausado con {self.tiempo_restante} segundos restantes.")

    def mostrar_tiempo(self):
        print(f"Tiempo restante: {self.tiempo_restante} segundos.")
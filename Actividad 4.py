class Termostato:
    def __init__(self, temperatura_inicial):
        self.temperatura = temperatura_inicial

    def aumentar_temperatura(self, grados):
        self.temperatura += grados

    def disminuir_temperatura(self, grados):
        self.temperatura -= grados

    def mostrar_temperatura(self):
        print(f"La temperatura actual es {self.temperatura}°C.")
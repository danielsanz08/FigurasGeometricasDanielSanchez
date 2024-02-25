from Figuras import Figura
import math

class Circulo(Figura):
    def __init__(self, radio: float =0):
        super().__init__("Circulo", 0)
        self.__radio = radio
    @property
    def radio(self):
        return self.__radio
    @radio.setter
    def radio(self, radio: float):
        self.__radio = radio

    def calcular_area(self):
        if self.radio is not None:
            self.area= math.pi * (self.radio ** 2)
            return self
    def __str__(self):
        return f"Nombre: {self.nombre}, Area: {self.area}, Radio: {self.radio}"
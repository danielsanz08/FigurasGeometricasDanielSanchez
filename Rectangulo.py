from Figuras import Figura

class Rectangulo(Figura):
    def __init__(self, altura: float, base: float):
        super().__init__("Rectangulo", 0)
        self.altura = altura
        self.base = base

    @property
    def altura(self) -> float:
        return self.__altura
    @altura.setter
    def altura(self, altura: float):
        self.__altura = altura

    @property
    def base(self) ->float:
        return self.__base

    @base.setter
    def base(self, base: float):
        self.__base = base

    def calcular_area(self)->float:
        if self.__base is None or self.__altura is None:
            print("No se puede calcular el area del triangulo")
            return False
        else:
            self.area = (self.base * self.altura)/2
            return self
    def __str__(self):
        return f"Nombre: {self.nombre}, Area: {self.area}, Altura: {self.altura}, Base: {self.base}"

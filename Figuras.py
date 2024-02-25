from abc import ABC,abstractmethod
class Figura(ABC):
    def __init__(self, nombre: str, area: float) :
        self.nombre = nombre
        self.area = area

    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: float):
        self.__nombre = nombre

    @property
    def area(self) ->float:
        return self.__area
    @area.setter
    def area(self, area: float):
        self.__area = area

    @abstractmethod
    def calcular_area(self):
        raise NotImplementedError
        pass
    def __str__(self):
        return f'Nombre: {self.nombre}, Area: {self.area}'
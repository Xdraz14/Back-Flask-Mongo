from abc import ABCMeta

class AbstractModelo(metaclass=ABCMeta):
    def __init__(self,data):
        for llave, valor in data.items(): #define como se recibiran los datos, en forma de diccionario, donde obtendra una llave valor
            setattr(self, llave, valor)
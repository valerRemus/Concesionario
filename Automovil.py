import json


class Automovil:

    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio


class CodificadorAutomovil(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, Automovil):
            return o.__dict__
        return super().default(o)
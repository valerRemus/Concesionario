import json
import os
from Automovil import Automovil, CodificadorAutomovil

#A veces hago ficheros como este donde voy probando los cambios y despues los añado a la version oficial.

class Concesionario:

    dir = r"C:\Users\r3mus\OneDrive\Escritorio\Proyectos\Concesionario"
    nombre_archivo = "concesionarios.json"
    ruta_archivo = os.path.join(dir, nombre_archivo)


    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.automoviles = []

    @staticmethod
    def crear_nuevo_concesionario(nombre,direccion):

        if os.path.exists(Concesionario.ruta_archivo):
            with open(Concesionario.ruta_archivo, "r") as archivo:
                datos_existentes = json.load(archivo)
                for datos in datos_existentes:
                    if nombre == datos["nombre"]:
                        raise Exception("El concesionario introducido ya existe :(")
                    elif nombre == "":
                        raise Exception("¡No puede estar vacio!")
                datos = Concesionario(nombre, direccion)
                datos_existentes.append(datos.__dict__)
        else:
            datos_existentes = [{"nombre": nombre, "direccion": direccion, "automoviles": []}]

        with open(Concesionario.ruta_archivo, "w") as archivo:
            json.dump(datos_existentes, archivo, indent=4)


    @staticmethod
    def agregar_modelo_a_concesionario(marca, modelo, anio, precio, concesionario):
        encontrado = False

        with open(Concesionario.ruta_archivo, "r") as archivo:
            datos_existentes = json.load(archivo)
            for datos in datos_existentes:
                if datos["nombre"].lower() == concesionario.lower():
                    datos["automoviles"].append(Automovil(marca, modelo, anio, precio))
                    encontrado = True

        if not encontrado:
            raise Exception("El concesionario no se ha encontrado")

        with open(Concesionario.ruta_archivo, "w") as archivo:
            json.dump(datos_existentes, archivo, cls=CodificadorAutomovil, indent=4)


    @staticmethod
    def mostrar_autos_venta(concesionario):

        with open(Concesionario.ruta_archivo, "r") as archivo:
            datos_existentes = json.load(archivo)
            for datos in datos_existentes:
                if datos["nombre"] == concesionario:
                    for i, valor in enumerate(datos["automoviles"]):

                        print(f"#####Auto {i+ 1} #####")
                        print(f"Marca: {valor['marca']}")
                        print(f"Modelo: {valor['modelo']}")
                        print(f"Año: {valor['anio']}")
                        print(f"Precio: {valor['precio']}")

    @staticmethod
    def buscar_auto():

        concesionario = input("Introduce el concesionario que quieres visitar: ")
        marca = input("Introduce la marca del vehículo: ")
        modelo = input("Introduce el modelo: ")

        with open(Concesionario.ruta_archivo, "r") as archivo:
            datos_existentes = json.load(archivo)
            for datos in datos_existentes:
                if concesionario == datos["nombre"]:
                    lista_autos = datos["automoviles"]
                    for auto in lista_autos:
                        if auto["marca"] == marca and auto["modelo"] == modelo:
                            print("#### Auto encontrado ####")
                            print(f"Marca: {auto['marca']}")
                            print(f"Modelo: {auto['modelo']}")
                            print(f"Año: {auto['anio']}")
                            print(f"Precio: {auto['precio']}")

    @staticmethod
    def vender_auto():
        concesionario = input("Introduce el concesionario: ")

        with open(Concesionario.ruta_archivo, "r") as archivo:
            datos_existentes = json.load(archivo)
            for datos in datos_existentes:
                if datos["nombre"] == concesionario:
                    autos = datos["automoviles"]
                    for i, auto in enumerate(autos):
                        print(f"{i + 1}. {auto['marca']} {auto['modelo']}")
                    vendido = int(input("Introduce el índice del coche a vender: "))
                    del autos[vendido - 1]
                    print("¡Coche vendido!")

        with open(Concesionario.ruta_archivo, "w") as archivo:
            json.dump(datos_existentes, archivo, cls=CodificadorAutomovil, indent=4)
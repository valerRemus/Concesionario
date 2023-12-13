import json
import os
from Automovil import Automobile, AutomobileEncoder

class Concesionario:

    dir = r"C:\Users\r3mus\OneDrive\Escritorio\Proyectos\Concesionario"
    file_name = "concesionarios.json"
    file_path = os.path.join(dir, file_name)


    def __init__(self, name, direction):
        self.name = name
        self.direction = direction
        self.automobiles = []

    @staticmethod
    def create_new_concessionaire():

        name = input("Introduce el nombre del concesionario: ")
        direction = input("Introduce la direccion del concesionario: ")

        if os.path.exists(Concesionario.file_path):
            with open(Concesionario.file_path, "r") as file:
                existing_data = json.load(file)
                for data in existing_data:
                    if name == data["name"]:
                        raise Exception("El Concesionario introducido ya existe")
                data = Concesionario(name, direction)
                existing_data.append(data.__dict__)
        else:
            existing_data = [{"name": name, "direction": direction, automobiles: []}]

        with open(Concesionario.file_path, "w") as file:
            json.dump(existing_data, file, indent = 4)
        print("¡Concesionario creado correctamente!")
    @staticmethod
    def add_model_to_concessionaire():

        brand = input("Introduce la marca del vehiculo: ")
        model = input("Introduce el modelo del vehiculo: ")
        year = input("Introduce el año del vehiculo: ")
        price = input("Introduce el precio del vehiculo: ")
        concessionaire = input("Introduce el nombre del concesionario: ")

        with open(Concesionario.file_path, "r") as file:
            existing_data = json.load(file)
            for data in existing_data:
                if data["name"] == concessionaire:
                    data["automobiles"].append(Automobile(brand,model,year,price))

        with open(Concesionario.file_path, "w") as file:
            json.dump(existing_data, file, cls=AutomobileEncoder, indent= 4)
        print("¡Vehiculo añadido correctamente!")
    @staticmethod
    def show_selling_cars():

        concesionario = input("Introduce el concesionario que quieres visitar: ")
        with open(Concesionario.file_path, "r") as file:
            existing_data = json.load(file)
            for data in existing_data:
                if data["name"] == concesionario:
                    for i, value in enumerate(data["automobiles"]):
                        print(f"#####Car {i+ 1} #####")
                        print(f"Brand: {value['brand']}")
                        print(f"Model: {value['model']}")
                        print(f"Year: {value['year']}")
                        print(f"Price: {value['price']}")

    @staticmethod
    def search_car():

        concesionario = input("Introduce el concesionario que quieres visitar: ")
        brand = input("Introduce la marca del vehiculo: ")
        model = input("Introduce el modelo: ")

        with open(Concesionario.file_path, "r") as file:
            existing_data = json.load(file)
            for data in existing_data:
                if concesionario == data["name"]:
                    carlist = data["automobiles"]
                    for automobil in carlist:
                        if automobil["brand"] == brand and automobil["model"] == model:
                            print("#### Vehiculo encontrado ####")
                            print(f"Brand: {automobil['brand']}")
                            print(f"Model: {automobil['model']}")
                            print(f"Year: {automobil['year']}")
                            print(f"Price: {automobil['price']}")

    @staticmethod
    def sell_car():
        concesionario = input("Introduce el concesionario: ")

        with open(Concesionario.file_path, "r") as file:
            existing_data = json.load(file)
            for data in existing_data:
                if data["name"] == concesionario:
                    cars = data["automobiles"]
                    for i,car in enumerate(cars):
                        print(f"{i + 1}. {car['brand']} {car['model']}")
                    sold = int(input("Introduce el indice del coche a vender: "))
                    del cars[sold - 1]
                    print("¡Coche vendido!")

        with open(Concesionario.file_path, "w") as file:
            json.dump(existing_data,file, cls=AutomobileEncoder, indent= 4)


import Concesionario

while True:
    print("#### MENU #####")
    print("1. Crear concesionario.")
    print("2. Añadir automovil.")
    print("3. Buscar automovil")
    print("4. Vender automovil.")
    print("5. Mostrar automoviles disponibles.")
    print("6. Salir")
    opc = int(input("Seleccione opción: "))
    if opc not in range(1, 7):
        raise Exception("Opcion no valida")

    match opc:
        case 1:
            Concesionario.Concesionario.create_new_concessionaire()
        case 2:
            Concesionario.Concesionario.add_model_to_concessionaire()
        case 3:
            Concesionario.Concesionario.search_car()
        case 4:
            Concesionario.Concesionario.sell_car()
        case 5:
            Concesionario.Concesionario.show_selling_cars()
        case 6:
            print("¡Hasta luego!")
            break



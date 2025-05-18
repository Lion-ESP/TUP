
"""
MISION VIERNES 1
Desarrollar un algoritmo que determine si una persona es inimputable o no. Informar mediante mensajes si el usuario sigue el procedimiento correctamente. Contemplar todos los posibles casos mediante el uso de las estructuras condicionales vistas en clase (if, elif, else). 

"""
posible_robo = False
opcion = 0

posible_robo = input("Le entraron a robar a tu casa?: Y/N ").strip().lower()


if posible_robo in ("N", "n", "no", "not"):
    print("No existe el robo")
else:
    while opcion == 0:
        print("Elija una opcion: ")
        print("1- Lo amasijaste en el patio? ")
        print("2- Lo llevaste al lugar más recondito de la casa? ")
        opcion = int(input("-> "))

match opcion:
    case 1:
        print("Te comes un garron de la gran flauta por que el ladron se cayó de la medianera...")
    case 2:
        opcion = 0
        while opcion == 0:
            print("Elija una opcion: ")
            print("1- Le tiraste un solo tiro? ")
            print("2- Lo reventaste a balazos?? ")
            opcion = int(input("-> "))
        match opcion:
            case 1:
                print("Te comes un garron de la gran flauta por que le tiraste un solo tiro, serás conciderado habil tirador...")
            case 2:
                opcion = 0
                while opcion == 0:
                    print("1- Estabas en un estado de emoción violenta y de locura??? ")
                    print("2- Lo reventaste a tiros y le vaciaste el cargador??? ")
                    print("3- Lo measte??? ")
                    print("4- Tomaste wisky??? (Si tenes la del diego mandale tmb) ")
                    print("5- TODAS LAS ANTERIORES? ")
                    opcion = int(input("-> "))
                
                    match opcion:
                        case 1:
                            print("Vas bien, pero faltan cositas")
                            opcion = 0
                        case 2:
                            print("Vas bien, pero faltan cositas")
                            opcion = 0
                        case 3:
                            print("Vas bien, pero faltan cositas")
                            opcion = 0
                        case 4:
                            print("Vas bien, pero faltan cositas")
                            opcion = 0
                        case 5:
                            print("SOS ININPUTABLE HERMANO, EN 10 DÍAS SALÍS")
                        case _:
                            opcion = 0
                            print("Elija una opcion de la lista!!!")
    case 0:
        print("Safaste che")
    case _:
        print("Error")     


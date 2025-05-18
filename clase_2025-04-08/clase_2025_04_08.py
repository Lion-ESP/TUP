
"""
Identificar el día de la semana
Solicita al usuario que ingrese un número entero entre 1 y 7. 
Utiliza match-case para imprimir el nombre del día de la semana 
correspondiente (por ejemplo, 1 para "Lunes", 2 para "Martes", etc.). 
Si el número no está en ese rango, muestra un mensaje indicando que el número es inválido.
Agregar la siguiente funcionalidad luego:
En el dia Sabado o Domingo si la temperatura (debera soliciar al usuario) esta entre 20 y 30 grados, imprimir "Puedes salir de la ca
"Puedes salir de la casa",
si la temperatura es mayor a 30 grados, imprimir "No puedes salir de la casa porque hace mucho calor",
si la temperatura es menor a 20 grados, imprimir "No puedes salir de la casa porque hace mucho frio".
"""


dia = int(input("ingrese un numero del 1 al 7 los cuales equivalen a los días de la semana: "))

if dia < 1 or dia > 7:
    print("Numero fuera de rango, error.")
else:
    match dia:
        case 1:
            print("1- Lunes")
        case 2:
            print("2- Martes")
        case 3:
            print("3- Miercoles")
        case 4:
            print("4- Jueves")
        case 5:
            print("5- Viernes")
        case 6 | 7:
            if dia == 6:
                print("6- Sabado")
            else: 
                print("7- Domingo")
        case _:
            print("Valor fuera de rango")
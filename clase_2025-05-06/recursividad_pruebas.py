'''
Debe crear un programa que permita ingresar una edad (entre 1 y 99 años, validar mediante una funcion) y un género (‘F’, ‘M’,  ‘X’, validar mediante una funcion). En caso de ingresar valores erróneos (edad fuera de rango, o generos inexistentes), informar de esa situación mostrando un mensaje y terminar el programa. Si todos los datos fueron bien ingresados, el programa debe ser capas de indicar, sabiendo que las mujeres se jubilan a los 60 años o mas, los hombres con 65 años o mas, para los no binarios establecemos un promedio de ambas edades. Determinar mediante funciones si una persona puede o no jubilarse.
validar_edad(edad)
'''

##Realizar una función recursiva que calcule la suma de los primeros números naturales
##Crea una función recursiva que sume los números naturales, o sea, la suma de 1 hasta un número dado n

def sumar_naturales(numero: int)->int:
    if numero == 1:
        return 1
    else:
        return numero + sumar_naturales(numero - 1)

#print(sumar_naturales(5))

#1 + 2 + 3 + 4 + 5 =  3 + 3 = 6 

#Realizar una función recursiva que calcule la potencia de un número:
#125 = 5 * 5 * 5

def calcular_potencia(base: int, exponente: int)->int:
    if exponente == 1:
        return base
    else:
        return base * calcular_potencia(base, exponente - 1)

#print(calcular_potencia(5,3))

#Realizar una función recursiva que permita realizar la suma de los dígitos de un número:
# tiene que ser un numero >= 10
# ejemplo (25) --> 2 + 5 = 7
# ejemplo (234) --> 2 + 3 + 4 = 9
#print(12//10) => devuelve el primer número
#print(12%10) => devuelve el segundo número


def sumar_digitos(numero: int)->int:
    if numero < 10:
        return numero
    else: 
        return (numero%10) + sumar_digitos(numero//10) # 23

print(sumar_digitos(234))

print("ejemplos \n")
print(25//10) 
print(25%10) 
print((25//10) + (25%10))
print((2//10))
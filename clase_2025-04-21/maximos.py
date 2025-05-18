import math

'''' 
8-Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
9-Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado. (se puede intentar hacer con pow() que esta en math)
'''


def maximo_de_tres(num1,num2,num3):
    mas_grande = 0

    if num1 > num2 and num1 > num3:
        mas_grande = num1
    elif num2 > num1 and num2 > num3:
        mas_grande = num2
    else:
        mas_grande = num3
    
    return mas_grande

num1 = float(input("Ingrese el primer numero a evaluar: "))
num2 = float(input("Ingrese el primer segundo a evaluar: "))
num3 = float(input("Ingrese el primer tercero a evaluar: "))

print(f"El numero más grande es {maximo_de_tres(num1, num2, num3)}")

def calcular_potencia(base, exponente):
    return pow(base, exponente)

base = float(input("Ingrese la base a evaluar: "))
expo = float(input("Ingrese el exponente evaluar: "))

print(f"Metodo con funcion pow: {calcular_potencia(base, expo)}")


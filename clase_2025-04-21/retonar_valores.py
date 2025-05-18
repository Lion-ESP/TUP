    # 1-Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
    # 2-Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
    # 3-Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 


def retornar_int():
    num = int(input("ingrese el numero: "))
    print(type(num))
    return num
    
def retornar_float():
    num = float(input("ingrese el numero: "))
    print(type(num))
    return num

def retornar_string():
    num = input("ingrese el numero: ")
    print(type(num))
    return num

def retornar_entero(mensaje = "Ingrese un numero"):
    
    print(type(num))
    return num
    
    
print(retornar_int())
print(retornar_float())
print(retornar_string())


#alternativa
num = input("ingrese un numero cualquiera: ")

print(retornar_entero(num))



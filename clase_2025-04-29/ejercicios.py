
# 1- Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
def crear_array_numeros (cant_elementos):
    """ Función que define la cantidad de elementos
    
    Args: 
    cantidad de elementos ingresada por el usuario
    
    Returns: 
    una lista inicializada """
    array_numeros = [0] * cant_elementos
    return array_numeros

# 3- Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
def calcular_promedios (array_numeros):
    """ Función que calcula el promedio de todos los elementos de una lista

    Args: 
    Una lista de numeros enteros ingresados por el usuario 
    
    Returns: 
    El resultado del promedio de todos los elementos de la lista """
    acumulador = 0
    for i in range(len(array_numeros)):
        acumulador += array_numeros[i] 
        
    promedio = acumulador / len(array_numeros)
    return promedio

# 4 - Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
def calcular_promedios_positivos (array_numeros):
    """ Función que calcula el promedio de todos los elementos positivos de una lista

    Args: 
    Una lista de numeros enteros positivos ingresados por el usuario.
    Ademas indica cuales numeros no se procesaron.
    
    Returns: 
    El resultado del promedio de todos los numeros positivos de la lista """
    acumulador = 0
    for i in range(len(array_numeros)):
        if array_numeros[i] > 0:
            acumulador += array_numeros[i] 
        else: print(f"No se calcula el numero {array_numeros[i]}")

    promedio = acumulador / len(array_numeros)
    return promedio

# 5 - Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
def calcular_producto (array_numeros):
    """ Función que calcula el producto de todos los elementos de una lista

    Args: 
    Una lista de numeros enteros ingresados por el usuario 
    
    Returns: 
    El resultado del producto de todos los elementos de la lista """
    acumulador = 1
    for i in range(len(array_numeros)):
        acumulador *= array_numeros[i]  # 1 * 1 = 1, acumulador = 1 * 5  = 5 * 5 = 25 * 2 = 50
    producto = acumulador
    return producto

# 6 - Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
def posicion_maxima (array_numeros):
    """ Función que encuentra la posicion del numero mas grande de todos los numeros enteros de una lista.

    Args: 
    Una lista de numeros enteros ingresados por el usuario.
    
    Returns: 
    La posicion del numero mas grande"""
    numero_maximo = 0
    for i in range(len(array_numeros)): ## 1, 4, 2
        if array_numeros[i] > numero_maximo: # 1, 4, 2
            numero_maximo = array_numeros[i]
            print(f"Valor analizado maximo {numero_maximo}")
            posicion_var_max = i
        else: print(f"El valor {array_numeros[i]} no es mas grande que el valor {numero_maximo}")
    return posicion_var_max

cant_elementos = int(input("Ingrese cantidad de elementos: "))
array_numeros = crear_array_numeros(cant_elementos)

print(array_numeros)

for i in range(len(array_numeros)):
    array_numeros[i] = int(input("Ingrese un numero entero: "))

promedio = calcular_promedios(array_numeros)
print(f"El promedio de los numeros ingresados es: {promedio}")

pro_positivos = calcular_promedios_positivos(array_numeros)
print(f"El promedio de los numeros enteros positivos ingresados es: {pro_positivos}")

cal_producto = calcular_producto(array_numeros)
print(f"El producto de los numeros ingresados es: {cal_producto}")

pos_maxima = posicion_maxima(array_numeros)
print(f"La posicion del numero mas grande es: {pos_maxima}")




print("# Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.")
numero_ascendente = 10

for i in range (10):
    i += 1
    print(f"{i}")

print("# Mostrar 10 repeticiones de números descendentes desde el 10 al 1.")

for i in range (10):
    print(f"{numero_ascendente}")
    numero_ascendente -= 1

print("# Mostrar la suma de los números desde el 1 hasta el 10.")

numero_ascendente = 0

for i in range (1,11):
    numero_ascendente += i
    print(f"{numero_ascendente}")

#Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números positivos y el producto de los negativos.

acum_positivos = 0
acum_negativos = 1
eleccion = 'Y'

while eleccion == 'Y':
    ingreso_usuario = int(input("ingrese un numero: "))
    if (ingreso_usuario > 0):
        acum_positivos += ingreso_usuario
    elif (ingreso_usuario < 0):
        acum_negativos *= ingreso_usuario
##    print(f"Positivos: {acum_positivos}")
##    print(f"Negativos: {acum_negativos}")
    eleccion = input("Desea continuar? Y/N: ").upper()

print(f"Los resultados positivos son: {acum_positivos}")
if acum_negativos == 1:
    print(f"Los resultados negativos son: {acum_negativos - 1}")


#Ingresar 10 números enteros. Determinar el máximo y el mínimo.

print("#Ingresar 10 números enteros. Determinar el máximo y el mínimo.")

num_ingresado = 0
num_maximo = 0
num_minimo = 0

for i in range (10):
    num_ingresado = int(input("ingrese el numero: "))
    if num_ingresado > num_maximo:
        num_maximo = num_ingresado
    if num_ingresado < num_minimo:
        num_minimo = num_ingresado

print(f"Los resultados son: maximo: {num_maximo}, minimo: {num_minimo}")











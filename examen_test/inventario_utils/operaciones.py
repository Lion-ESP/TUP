

# SISTEMA DE ADMINISTRACION DE PRODUCTOS PARA ALMACENES

"""
PARA CADA PRODUCTO SE ALMACENARÁ:
NOMBRE -> str
PRECIO -> float
CANTIDAD -> int

EJEMPLO ARRAY:
inventario = [
    ["Laptop", 1500.00, 10],
    ["Silla", 200.00, 50],
    ["Libro", 15.00, 100],
    ["Monitor", 300.00, 30]
    [cadena, float, int]
]
"""

def menu_principal() -> None:
    inventario = []
    opcion_input = 0

    while opcion_input != 6:

        print("\nMenu Principal: ")
        print("1- Cargar productos.")
        print("2- Buscar producto.")
        print("3- Ordenar inventario.")
        print("4- Mostrar producto mas caro y más barato.")
        print("5- Mostrar productos con precio mayor a 15000.")
        print("6- Salir.")
        opcion_input = int(input("-> "))

        if opcion_input.is_integer() and 0 < opcion_input <= 6: 

            match(opcion_input):
                case 1:
                    inventario = cargar_inventario(inventario)
                    mostrar_inventario(inventario)
                case 2:
                    buscar_producto(inventario)
                case 3:
                    ordenar_inventario_asc()
                    print("En desarrollo...")
                    pass
                case 4:
                    mostrar_producto_mas_caro(inventario)
                    mostrar_producto_mas_barato(inventario)
                case 5:
                    producto_con_precio_mayor_quincemil(inventario)
                case 6:
                    return
                case _:
                    print("error")
        else:
                print("Opcion incorrecta\n Por favor ingrese un número entre 1 y 6.")


def cargar_inventario(inventario: list) -> list:
    """
    - Ingreso de datos de 1 o mas producto a un inventario.

    Parametros:
    - Un inventario inicializado. 

    Retorna:
    - Un inventario construido con los datos ingresados por el usuario.
    """
    cantidad_productos = None
    while cantidad_productos is None:
        cantidad_productos = int(input("Ingrese la cantidad de productos que desea cargar:"))
        if cantidad_productos <= 0:
            print("Error: La cantidad de productos debe ser mayor a cero.")
            return []
    
    for i in range(cantidad_productos):
        print(f"\nProducto {i + 1}:")
        
        nombre = input("Ingrese el nombre del producto: ")
        
        precio = None
        while precio is None:
                precio = float(input("Ingrese el precio del producto: "))
                if precio < 0:
                    print("Ingrese un precio positivo")

        cantidad = None
        while cantidad is None:
                cantidad = int(input("Ingrese la cantidad disponible: "))
                if cantidad < 0:
                    print("Error: La cantidad no puede ser negativa.")
                    cantidad = None

        producto = [nombre, precio, cantidad]
        inventario = inventario + [producto] 
    
    print("\nInventario cargado correctamente.")
    return inventario

def mostrar_inventario(inventario: list) -> None:
    """
    - Muestra el inventario actual

    Parámetros:
    - inventario (list): Lista de productos a mostrar por terminal.

    Retorna:
    - Nada.
    """
    print("\n Inventario actual:")
    for i in range(len(inventario)):
        producto = inventario[i]
        print(f"{i+1} | {producto[0]} | ${producto[1]:.2f} | {producto[2]}")
    
def buscar_producto(inventario: list) -> None:
    """
    - Busca el producto por nombre en el inventario
    - Muestra todos los datos del producto encontrado (nombre, precio y cantidad).

    Parámetros:
    - inventario (list): Lista de productos inventariados.

    Retorna:
    - Nada.
    """
    if not inventario:
        print("\nEl inventario está vacío.")
        return
        
    nombre_buscar = input("\nIngrese el nombre del producto a buscar: ")
    encontrados = []
    
    for i in range(len(inventario)):
        if nombre_buscar.lower() == inventario[i][0].lower():
            encontrados = encontrados + [inventario[i]]
    
    if encontrados:
        print("\nProductos encontrados:")
        for producto in encontrados:
            print(f"{producto[0]} | ${producto[1]:.2f} | {producto[2]}")
    else:
        print(f"\nNo se encontraron productos con el nombre '{nombre_buscar}'.")

def mostrar_producto_mas_caro(inventario) -> None:
    """
    Busca el producto mas barato en una lista bidimencional.

    Parámetros:
    - inventario (list): Lista de productos con precio a eveluar.

    Retorna:
    - Nada.
    """
    if not inventario:
        print("\nEl inventario está vacío.")
        return
    
    producto_mas_caro = inventario[0]
    
    for i in range(1, len(inventario)):
        if inventario[i][1] > producto_mas_caro[1]:
            producto_mas_caro = inventario[i]
    
    print("\nProducto mas caro:")
    print(f"{producto_mas_caro[0]} | ${producto_mas_caro[1]:.2f} | {producto_mas_caro[2]}")


def mostrar_producto_mas_barato(inventario) -> None:
    """
    Busca el producto mas barato en una lista bidimencional.

    Parámetros:
    - inventario (list): Lista de productos con precio a eveluar.

    Retorna:
    - Nada.
    """
    if not inventario:
        print("\nEl inventario está vacío.")
        return
    
    producto_mas_barato = inventario[0]
    
    for i in range(1, len(inventario)):
        if inventario[i][1] < producto_mas_barato[1]:
            producto_mas_barato = inventario[i]
    
    print("\nProducto mas barato:")
    print(f"{producto_mas_barato[0]} | ${producto_mas_barato[1]:.2f} | {producto_mas_barato[2]}")

def producto_con_precio_mayor_quincemil(inventario: list) -> None:
    """
    Busca el precio con mayor valor en una lista bidimencional

    Parámetros:
    - inventario (list): Lista de productos con precio a eveluar.

    Retorna:
    - Nada.
    """
    if not inventario:
        print("\nEl inventario está vacío.")
        return
    
    for i in range(len(inventario)):
        for j in range(len(inventario[i])):
            if inventario[i][1] > 15000:
                producto_con_precio_mayor_quincemil = inventario[i]

    print("\nProducto con precio mayor a 15.000:")
    print(f"{producto_con_precio_mayor_quincemil[0]} | ${producto_con_precio_mayor_quincemil[1]:.2f} | {producto_con_precio_mayor_quincemil[2]}")

def ordenar_inventario_asc() -> None:
    pass
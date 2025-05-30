def cargar_inventario(inventario: list) -> list:
    """
    - Ingreso de datos de 1 o mas producto a un inventario.

    Parametros:
    - Un inventario inicializado. 

    Retorna:
    - Un inventario construido con los datos ingresados por el usuario.
    """
    debug = 1

    if debug != 1:
        cantidad_productos = None
        while cantidad_productos == None:
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
    else:
        inventario = [
            ["Laptop", 15500, 10],
            ["Silla", 200, 50],
            ["Libro", 15, 100],
            ["Monitor", 300, 30]              
        ]
    
    print("\nInventario cargado correctamente.")
    return inventario

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
        print(f"{i+1} | {producto[0]} | ${producto[1]} | {producto[2]}")

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
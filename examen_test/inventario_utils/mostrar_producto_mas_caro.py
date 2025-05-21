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
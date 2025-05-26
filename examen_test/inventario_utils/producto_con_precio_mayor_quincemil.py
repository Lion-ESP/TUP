def filtrar_producto_con_precio_mayor_quincemil(inventario: list) -> list:
    """
    Busca el precio con mayor valor en una lista bidimencional

    Parámetros:
    - inventario (list): Lista de productos con precio a eveluar.

    Retorna:
    - Nada.
    """
    QUINCEMIL = 15000
    if not inventario:
        print("\nEl inventario está vacío.")
        return
    
    nuevo_inventario = []
    for i in range(len(inventario)):
        if inventario[i][1] > QUINCEMIL:
            nuevo_inventario = nuevo_inventario + [inventario[i]]
    
    return nuevo_inventario

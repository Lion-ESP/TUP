def producto_con_precio_mayor_quincemil(inventario: list) -> None:
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
    
    for i in range(len(inventario)):
        for j in range(len(inventario[i])):
            if inventario[i][1] > QUINCEMIL:
                producto_con_precio_mayor_quincemil = inventario[i]

    print(f"\nProducto con precio mayor a {QUINCEMIL}:")
    print(f"{producto_con_precio_mayor_quincemil[0]} | ${producto_con_precio_mayor_quincemil[1]:.2f} | {producto_con_precio_mayor_quincemil[2]}")

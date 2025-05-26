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
        if nombre_buscar == inventario[i][0]:
            encontrados = encontrados + [inventario[i]]
    
    if encontrados:
        print("\nProductos encontrados:")
        for producto in encontrados:
            print(f"{producto[0]} | ${producto[1]:.2f} | {producto[2]}")
    else:
        print(f"\nNo se encontraron productos con el nombre '{nombre_buscar}'.")
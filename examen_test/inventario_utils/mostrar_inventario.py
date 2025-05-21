
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
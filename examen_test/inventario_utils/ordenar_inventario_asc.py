from inventario_utils.mostrar_segun_filtros import mostrar_inventario as mostrar

def ordenar_inventario_asc(inventario: list) -> None:
    """
    - Ordena el inventario de forma descendente.

    Parametros:
    - inventario: list -> lista de productos inventariados.

    Retorna:
    - Nada
    """
    for i in range(len(inventario) - 1):
        for j in range(len(inventario) - 1 - i):
            if inventario[j][1] > inventario[j + 1][1]:
                aux = inventario[j]
                inventario[j] = inventario[j + 1]
                inventario[j + 1] = aux
                
    mostrar(inventario)
from inventario_utils.menu import menu_principal as menu
from inventario_utils.cargar_inventario import cargar_inventario as carga
from inventario_utils.mostrar_segun_filtros import mostrar_inventario as mostrar
from inventario_utils.buscar_producto import buscar_producto as buscar
from inventario_utils.ordenar_inventario_asc import ordenar_inventario_asc as ordenar
from inventario_utils.mostrar_segun_filtros import mostrar_producto_mas_caro as mas_caro
from inventario_utils.mostrar_segun_filtros import mostrar_producto_mas_barato as mas_barato
from inventario_utils.producto_con_precio_mayor_quincemil import filtrar_producto_con_precio_mayor_quincemil as mayores_quincemil

# SISTEMA DE ADMINISTRACION DE PRODUCTOS PARA ALMACENES

inventario = []
opcion_input = 0

while opcion_input != 6:

    opcion_input = menu()

    if 0 < opcion_input <= 6: 

        match(opcion_input):
            case 1:
                inventario = carga(inventario)
                mostrar(inventario)
            case 2:
                buscar(inventario)
            case 3:
                ordenar(inventario)
            case 4:
                mas_caro(inventario)
                mas_barato(inventario)
            case 5:
                nuevo_inventario = mayores_quincemil(inventario)
                print("\nSe filtrar los productos mayor a 15.000...")
                mostrar(nuevo_inventario)
            case 6:
                break
            case _:
                print("error")
    else:
            print("Opcion incorrecta\n Por favor ingrese un número entre 1 y 6.")
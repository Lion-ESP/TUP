from inventario_utils import menu
from inventario_utils import cargar_inventario
from inventario_utils import mostrar_inventario
from inventario_utils import buscar_producto
from inventario_utils import ordenar_inventario_asc
from inventario_utils import mostrar_producto_mas_caro
from inventario_utils import mostrar_producto_mas_barato
from inventario_utils import producto_con_precio_mayor_quincemil

# SISTEMA DE ADMINISTRACION DE PRODUCTOS PARA ALMACENES

inventario = []
opcion_input = 0

while opcion_input != 6:

    opcion_input = menu.menu_principal()


    if 0 < opcion_input <= 6: 

        match(opcion_input):
            case 1:
                inventario = cargar_inventario.cargar_inventario(inventario)
                mostrar_inventario.mostrar_inventario(inventario)
            case 2:
                buscar_producto.buscar_producto(inventario)
            case 3:
                ordenar_inventario_asc.ordenar_inventario_asc(inventario)
            case 4:
                mostrar_producto_mas_caro.mostrar_producto_mas_caro(inventario)
                mostrar_producto_mas_barato.mostrar_producto_mas_barato(inventario)
            case 5:
                producto_con_precio_mayor_quincemil.producto_con_precio_mayor_quincemil(inventario)
            case 6:
                break
            case _:
                print("error")
    else:
            print("Opcion incorrecta\n Por favor ingrese un número entre 1 y 6.")


# Caso de uso
if __name__ == "__main__":
    print("Fin.")
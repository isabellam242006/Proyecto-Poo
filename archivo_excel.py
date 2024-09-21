from producto import *
from inventario import *
import pandas as pd
import os

def guardar_inventario_excel(inventario, archivo="inventario.xlsx"):
    """Guarda el inventario en un archivo Excel usando pandas."""
    data = []

    # Recorremos los productos para crear una lista de diccionarios con sus atributos
    for nombre, producto in inventario.lista_productos.items():
        producto_data = {
            "Nombre": producto.nombre,
            "Precio por Unidad": producto.precio_unidad,
            "Unidades": producto.unidades,
            "Marca": producto.marca,
            "Fecha de Ingreso": producto.fecha_ingreso.strftime("%Y-%m-%d %H:%M:%S") if producto.fecha_ingreso else None,
            "Fecha de Última Actualización": producto.fecha_ultima_actualizacion.strftime("%Y-%m-%d %H:%M:%S") if producto.fecha_ultima_actualizacion else None,
            "Fecha de Vencimiento": producto.fecha_vencimiento.strftime("%Y-%m-%d") if producto.fecha_vencimiento else None
        }

        data.append(producto_data)

    # Crear un DataFrame con los datos
    df = pd.DataFrame(data)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel(archivo, index=False)
    print(f"Inventario guardado en el archivo {archivo} con éxito.")

print(os.getcwd())

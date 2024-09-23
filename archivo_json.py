import json
from datetime import datetime
from inventario import Inventario, Producto

# Función para serializar objetos datetime como cadenas
def serializar_datetime(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")  # Convierte datetime a string
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# Función para convertir una cadena a datetime
def deserializar_datetime(fecha_str):
    if fecha_str:
        try:
            return datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print(f"Error al convertir '{fecha_str}' a datetime.")
    return None

# Función para guardar el inventario en un archivo JSON
def guardar_inventario_json(inventario, archivo="inventario.json"):
    """Guarda el inventario en un archivo JSON."""
    try:
        with open(archivo, 'w') as f:
            productos = {}
            for k, producto in inventario.lista_productos.items():
                productos[k] = {
                    "nombre": producto.nombre,
                    "precio_costo_unidad": producto.precio_costo_unidad or 0,
                    "precio_venta_unidad": producto.precio_venta_unidad or 0,
                    "precio_venta_total": producto.precio_venta_total or 0, 
                    "unidades": producto.unidades or 0,
                    "unidades_vendidas": producto.unidades_vendidas or 0,  
                    "marca": producto.marca or "",
                    "fecha_ingreso": serializar_datetime(producto.fecha_ingreso) if producto.fecha_ingreso else "",
                    "fecha_actualizacion": serializar_datetime(producto.fecha_actualizacion) if producto.fecha_actualizacion else "",
                    "fecha_vencimiento": serializar_datetime(producto.fecha_vencimiento) if producto.fecha_vencimiento else ""
                }
            json.dump(productos, f, indent=4)
        print(f"Inventario guardado en el archivo {archivo}.")
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

# Función para cargar los productos desde un archivo JSON
def cargar_inventario_json(archivo="inventario.json"):
    """Carga los productos desde un archivo JSON al inventario."""
    inventario = Inventario()
    try:
        with open(archivo, 'r') as f:
            productos = json.load(f)
            for nombre, datos in productos.items():
                producto = Producto(
                    nombre=datos['nombre'],
                    precio_costo_unidad=datos['precio_costo_unidad'],
                    precio_venta_unidad=datos['precio_venta_unidad'],
                    unidades=datos['unidades'],
                    marca=datos['marca'],
                    fecha_vencimiento=deserializar_datetime(datos.get('fecha_vencimiento', None))
                )
                producto.fecha_ingreso = deserializar_datetime(datos.get('fecha_ingreso', None))
                producto.fecha_actualizacion = deserializar_datetime(datos.get('fecha_actualizacion', None))
                producto.precio_venta_total = datos.get('precio_venta_total', 0)  
                producto.unidades_vendidas = datos.get('unidades_vendidas', 0)  
                inventario.registrar_entrada(producto)
        print(f"Inventario cargado desde {archivo} con éxito.")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Empezando con un inventario vacío.")
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
    return inventario




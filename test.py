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
            productos = {k: v.__dict__ for k, v in inventario.lista_productos.items()}
            json.dump(productos, f, indent=4, default=serializar_datetime)
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
                inventario.registrar_entrada(producto)
        print(f"Inventario cargado desde {archivo} con éxito.")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Empezando con un inventario vacío.")
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
    return inventario

def clasificar_abc(self):
        """Clasifica los productos en A, B, o C según el índice de rotación o ingresos."""
        productos = list(self.inventario.lista_productos.values())

        # Ordenar productos por ingresos (de mayor a menor)
        productos.sort(key=lambda producto: producto.precio_venta_total, reverse=True)

        total_ingresos = self.calcular_ingresos()
        acumulado_ingresos = 0

        clasificacion = {}

        # Clasificar en A, B, C
        for producto in productos:
            porcentaje_acumulado = (acumulado_ingresos / total_ingresos) * 100 if total_ingresos > 0 else 0

            if porcentaje_acumulado < 80:  # Categoría A (primer 80% de ingresos)
                clasificacion[producto.nombre] = 'A'
            elif porcentaje_acumulado < 95:  # Categoría B (entre 80% y 95%)
                clasificacion[producto.nombre] = 'B'
            else:  # Categoría C (último 5% de ingresos)
                clasificacion[producto.nombre] = 'C'

            acumulado_ingresos += producto.precio_venta_total

        print("Clasificación ABC de los productos:")
        for nombre, categoria in clasificacion.items():
            print(f"Producto: {nombre}, Categoría: {categoria}")

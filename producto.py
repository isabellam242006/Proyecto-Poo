import uuid  
from datetime import datetime, timedelta  
import random  

class Producto:
    """
    Clase que representa un producto dentro de un inventario.

    Atributos:
    ----------
    id : str
        Identificador único del producto generado automáticamente.
    nombre : str
        Nombre del producto.
    precio : float
        Precio del producto.
    cantidad : int
        Cantidad disponible del producto en el inventario.
    fecha_ingreso : datetime
        Fecha en que el producto ingresó al inventario. Esta fecha se mantiene estática.
    fecha_actualización : datetime
        Fecha de la última vez que se actualizó la cantidad del producto.
    fecha_vencimiento : datetime
        Fecha estimada de vencimiento o caducidad del producto, generada aleatoriamente.
    """

    def __init__(self, nombre, precio_costo_unidad, precio_venta_unidad, unidades, marca, fecha_vencimiento):
        """
        Inicializa una nueva instancia de la clase Producto.

        Parámetros:
        -----------
        nombre : str
            Nombre del producto.
        precio : float
            Precio del producto.
        cantidad : int
            Cantidad inicial del producto en inventario.

        Comportamiento:
        ---------------
        - Genera un ID único para cada producto usando uuid4().
        - Asigna la fecha actual como la fecha de ingreso.
        - Genera una fecha de vencimiento aleatoria entre 1 y 4 años a partir de la fecha actual.
        """
        self.id = str(uuid.uuid4())  
        self.nombre = nombre  
        self.precio_costo_unidad = precio_costo_unidad
        self.precio_venta_unidad = precio_venta_unidad
        self.unidades = unidades
        self.unidades_vendidas = 0
        self.precio_costo_total = precio_costo_unidad * unidades
        self.precio_venta_total = None
        self.marca = marca
        self.fecha_ingreso = None
        self.fecha_actualizacion = None
        self.fecha_vencimiento = fecha_vencimiento
        self.stock_inicial = unidades

    def __str__(self):
        """Define cómo se imprime un objeto Producto."""
        return f"Producto: {self.nombre}, Marca: {self.marca}"

    def __repr__(self):
        """Define una representación más detallada del objeto Producto."""
        return f"<Producto(nombre={self.nombre}, precio={self.precio_costo_unidad}, unidades={self.unidades})>"
    
    def detalles(self):
        return (f"Nombre: {self.nombre}\n"
                f"Marca: {self.marca}\n"
                f"Precio de costo del producto por unidad: {self.precio_costo_unidad}\n"
                f"Precio total del costo del producto: {self.precio_costo_total}\n"
                f"Precio de venta del producto por unidad: {self.precio_venta_unidad}\n"
                f"Precio total de venta del producto: {self.precio_venta_total}\n"
                f"Unidades disponibles: {self.unidades}\n"
                f"Unidades vendidas: {self.unidades_vendidas}\n"
                f"Fecha de ingreso: {self.fecha_ingreso}\n"
                f"Fecha de actualización: {self.fecha_actualizacion}\n"
                f"Fecha de vencimiento: {self.fecha_vencimiento}\n")
    


class FrutasYVerduras(Producto):
    def __init__(self, nombre, precio_costo_unidad, precio_venta_unidad, unidades, marca, fecha_vencimiento, estado_producto, peso_total):
        super().__init__(nombre, precio_costo_unidad, precio_venta_unidad, unidades, marca, fecha_vencimiento)
        self.estado_producto = estado_producto  
        self.peso_total = peso_total  

    def __str__(self):
        return (super().__str__() +  
                f"\nEstado del producto: {self.estado_producto}"
                f"\nPeso total: {self.peso_total} kg")

    def detalles(self):
        return (super().detalles() +
                f"Estado del producto: {self.estado_producto}\n"
                f"Peso del producto: {self.peso_total} kg\n")




class Congelados(Producto):
    def __init__(self, nombre, precio_costo_unidad, precio_venta_unidad, unidades, marca, fecha_vencimiento, temperatura):
        super().__init__(nombre, precio_costo_unidad, precio_venta_unidad, unidades, marca, fecha_vencimiento)
        self.temperatura = temperatura  
    
    def calcular_temperatura_optima(self):
        if self.temperatura != -18:
            print(f"Faltan {self.temperatura -(-18)} grados para llegar a la temperatura óptima (-18°C).")
        else:
            print("La temperatura es óptima.")
    
    def __str__(self):
        return (super().__str__() +  # Llama al __str__ de la clase padre (Producto)
                f"\nTemperatura: {self.temperatura}°C"
                f"\nTemperatura óptima: {self.calcular_temperatura_optima()}°C")

  
    def detalles(self):
        return (super().detalles() +
                f"Temperatura actual: {self.temperatura}°C\n"
                f"Temperatura óptima: {self.calcular_temperatura_optima()}°C\n")










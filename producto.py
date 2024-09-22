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

    def __init__(self, nombre, precio_unidad, unidades, marca, fecha_vencimiento):
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
        self.precio_unidad = precio_unidad
        self.unidades = unidades
        self.precio_total = precio_unidad * unidades
        self.marca = marca
        self.fecha_ingreso = None
        self.fecha_actualizacion = None
        self.fecha_vencimiento = fecha_vencimiento

    def __str__(self):
        """Define cómo se imprime un objeto Producto."""
        return f"Producto: {self.nombre}, Marca: {self.marca}"

    def __repr__(self):
        """Define una representación más detallada del objeto Producto."""
        return f"<Producto(nombre={self.nombre}, precio={self.precio_unidad}, unidades={self.unidades})>"
    
    def detalles(self):
        return (f"Nombre: {self.nombre}\n"
                f"Marca: {self.marca}\n"
                f"Precio por unidad: {self.precio_unidad}\n"
                f"Precio total: {self.precio_total}\n"
                f"Unidades disponibles: {self.unidades}\n"
                f"Fecha de ingreso: {self.fecha_ingreso}\n"
                f"Fecha de actualización: {self.fecha_actualizacion}\n"
                f"Fecha de vencimiento: {self.fecha_vencimiento}\n")
    


class FrutasYVerduras(Producto):
    def __init__(self, nombre, precio_unidad, unidades, marca, fecha_vencimiento, estado_producto, peso_total):
        super().__init__(nombre, precio_unidad, unidades, marca, fecha_vencimiento)
        self.estado_producto = estado_producto  # Estado del producto (fresco, podrido, etc.)
        self.peso_total = peso_total  # Peso total del producto en kilogramos

    def detalles(self):
        return (super().detalles() +
                f"Estado del producto: {self.estado_producto}\n"
                f"Peso total: {self.peso_total} kg\n")



class Congelados(Producto):
    def __init__(self, nombre, precio_unidad, unidades, marca, fecha_vencimiento, temperatura):
        super().__init__(nombre, precio_unidad, unidades, marca, fecha_vencimiento)
        self.temperatura = temperatura  # Temperatura a la que está el producto

    def detalles(self):
        return (super().detalles() +
                f"Temperatura actual: {self.temperatura}°C\n")



class Empaquetados(Producto):
    def __init__(self, nombre, precio_unidad, unidades, marca, fecha_vencimiento, calidad_empaque, peso_neto):
        super().__init__(nombre, precio_unidad, unidades, marca, fecha_vencimiento)
        self.calidad_empaque = calidad_empaque  # Calidad del empaque
        self.peso_neto = peso_neto  # Peso neto del producto en kilogramos

    def detalles(self):
        return (super().detalles() +
                f"Calidad del empaque: {self.calidad_empaque}\n"
                f"Peso neto: {self.peso_neto} kg\n")



if __name__ == "__main__":
    producto_1 = Producto("Arroz", 5000, 100, "Diana", datetime(2023, 12, 31))
    producto_2 = Producto("Papa", 1000, 200, "Sabritas" , datetime(2023, 12, 31))
    producto_3 = Producto("Leche", 2000, 50, "Alpina" , datetime(2023, 12, 31))
    producto_4 = Producto("Cereal", 3000, 150, "Zucaritas" , datetime(2023, 12, 31))



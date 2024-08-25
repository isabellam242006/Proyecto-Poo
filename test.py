import uuid
from datetime import datetime, timedelta
import random

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.id = str(uuid.uuid4())  # ID único generado automáticamente
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_ingreso = datetime.now()  # Fecha de ingreso fija en la creación del producto
        self.fecha_actualización = datetime.now()  # Fecha de actualización inicial
        self.fecha_vencimiento = datetime.now() + timedelta(days=random.randint(1, 365 * 4))  # Fecha de vencimiento aleatoria

    def actualizar_cantidad(self, cantidad):
        """
        Actualiza la cantidad del producto y la fecha de actualización.

        Parámetros:
        -----------
        cantidad : int
            Cantidad a agregar al stock del producto. Puede ser positiva o negativa.
        """
        self.cantidad += cantidad  # Actualiza la cantidad de forma acumulativa
        self.fecha_actualización = datetime.now()  # Actualiza la fecha de modificación

    def productos(self):
        """
        Devuelve una representación en cadena de los detalles del producto.

        Retorna:
        --------
        str:
            Información detallada del producto, incluyendo su ID, nombre, precio, cantidades y fechas.
        """
        return (f"Nombre: {self.nombre}\n"
                f"Precio: {self.precio}\n"
                f"Cantidad: {self.cantidad}\n"
                f"ID: {self.id}\n"
                f"Fecha de Ingreso: {self.fecha_ingreso}\n"
                f"Fecha de Actualización: {self.fecha_actualización}\n"
                f"Fecha de Vencimiento: {self.fecha_vencimiento}")

# Crear productos
producto_1 = Producto("Arroz", 5000, 100)
producto_2 = Producto("Papa", 1000, 200)
producto_3 = Producto("Leche", 2000, 50)
producto_4 = Producto("Cereal", 3000, 150)

# Imprimir los detalles del producto_1
print(producto_1.productos())

# Actualizar la cantidad del producto_1
producto_1.actualizar_cantidad(200)

# Imprimir los detalles del producto_1 nuevamente para verificar la actualización
print(producto_1.productos())

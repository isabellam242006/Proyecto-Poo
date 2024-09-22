from producto import Producto
from inventario import Inventario
from datetime import datetime

class AnalisisMonetario:
    def __init__(self, inventario):
        self.inventario = inventario  # Usar el inventario que ya contiene productos

    def calcular_ingresos(self):
        """Calcula el total de ingresos por la venta de productos."""
        total = sum([producto.precio_total for producto in self.inventario.lista_productos.values()])
        return total

# Crear productos
producto1 = Producto("Arroz", 5000, 100, "Diana", datetime(2023, 12, 31))
producto2 = Producto("Papa", 2000, 50, "La Rústica", datetime(2023, 12, 31))
producto3 = Producto("Leche", 3000, 150, "Alpina", datetime(2023, 12, 31))

# Crear inventario y agregar productos
inventario = Inventario()
inventario.registrar_entrada(producto1)
inventario.registrar_entrada(producto2)
inventario.registrar_entrada(producto3)

# Crear análisis monetario usando el inventario existente
analisis = AnalisisMonetario(inventario)

# Calcular e imprimir los ingresos
print(f"Total de ingresos: ${analisis.calcular_ingresos()}")

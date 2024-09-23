from producto import Producto
from inventario import Inventario
from datetime import datetime


class AnalisisMonetario:
    def __init__(self, inventario):
        self.inventario = inventario

        # Inicializar valores None como 0
        for producto in self.inventario.lista_productos.values():
            if producto.precio_venta_total is None:
                producto.precio_venta_total = 0
            if producto.precio_costo_total is None:
                producto.precio_costo_total = 0

    def calcular_ingresos(self):
        """Calcula el total de ingresos por las ventas."""
        total_ingresos = sum(producto.precio_venta_total for producto in self.inventario.lista_productos.values())
        return total_ingresos

    def calcular_costos(self):
        """Calcula el total de costos de los productos."""
        total_costos = sum(producto.precio_costo_total for producto in self.inventario.lista_productos.values())
        return total_costos

    def calcular_ganancias(self):
        """Calcula las ganancias como la diferencia entre ingresos y costos."""
        total_ingresos = self.calcular_ingresos()
        total_costos = self.calcular_costos()
        total_ganancias = total_ingresos - total_costos
        return total_ganancias
    
    def calcular_margen_ganancias(self):
        """Calcula el margen de ganancias como un porcentaje."""
        total_ganancias = self.calcular_ganancias()
        total_ingresos = self.calcular_ingresos()
        if total_ingresos > 0:
            margen_ganancias = (total_ganancias / total_ingresos) * 100
            return margen_ganancias
        else:
            return 0

    def calcular_inventario_promedio(self):
        """Calcula el inventario promedio de todos los productos."""
        stock_inicial = self.inventario.calcular_stock_inicial()
        stock_final = self.inventario.calcular_stock_final()

        inventario_promedio = (stock_inicial + stock_final) / 2
        return inventario_promedio

    def calcular_rotacion(self):
        """Calcula el índice de rotación del inventario."""
        total_ingresos = self.calcular_ingresos()
        inventario_promedio = self.calcular_inventario_promedio()
        if inventario_promedio > 0 and total_ingresos > 0:
            rotacion = total_ingresos / inventario_promedio
            return rotacion
        else:
            return 0

    def calcular_periodo_rotacion(self):
        """Calcula el periodo de rotación del inventario."""
        rotacion = self.calcular_rotacion()
        if rotacion > 0:
            periodo_rotacion = 365 / rotacion
            return periodo_rotacion
        else:
            return None

    def imprimir_resultados(self):
        """Imprime todos los resultados en una sola función."""
        total_ingresos = self.calcular_ingresos()
        total_costos = self.calcular_costos()
        total_ganancias = self.calcular_ganancias()
        margen_ganancias = self.calcular_margen_ganancias()
        inventario_promedio = self.calcular_inventario_promedio()
        rotacion = self.calcular_rotacion()
        periodo_rotacion = self.calcular_periodo_rotacion()

        print(f"Total de ingresos: {total_ingresos}")
        print(f"Total de costos: {total_costos}")
        print(f"Total de ganancias: {total_ganancias}")
        print(f"Margen de ganancias: {margen_ganancias}%")
        print(f"Inventario promedio: {inventario_promedio}")
        if rotacion > 0:
            print(f"Índice de rotación: {rotacion}")
        if periodo_rotacion:
            print(f"Periodo de rotación: {periodo_rotacion} días")



   






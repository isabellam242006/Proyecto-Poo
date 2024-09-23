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
            print("Margen de ganancias: ", margen_ganancias, "%")
        else:
            print("Aún no hay margen de ganancias.")
  
  
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
            print(f"El índice de rotación es: {rotacion}")
            return rotacion
        else:
            print("No se puede calcular el índice de rotación: inventario promedio o ingresos son 0.")
            return 0

 
    def calcular_periodo_rotacion(self):
        """Calcula el periodo de rotación del inventario."""
        rotacion = self.calcular_rotacion()
        if rotacion > 0:
            periodo_rotacion = 365 / rotacion
            print(f"El periodo de rotación es: {periodo_rotacion} días")
            return periodo_rotacion
        else:
            print("No se puede calcular el periodo de rotación: índice de rotación es 0.")
            return None
    
 
    def detalles(self):
        return (f"Ingresos totales: {self.calcular_ingresos()}\n"
                f"Costos totales: {self.calcular_costos()}\n"
                f"Ganancias totales: {self.calcular_ganancias()}\n"
                f"Margen de ganancias: {self.calcular_margen_ganancias()}\n"
                f"Inventario promedio: {self.calcular_inventario_promedio()}\n"
                f"Índice de rotación: {self.calcular_rotacion()}\n"
                f"Periodo de rotación: {self.calcular_periodo_rotacion()}\n")


   






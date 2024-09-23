from producto import Producto
from inventario import Inventario
from datetime import datetime

class AnalisisMonetario:
    def __init__(self, inventario):
        self.inventario = inventario  # Usar el inventario que ya contiene productos

    def calcular_ingresos(self):
        """Calcula el total de ingresos por las ventas."""
        total_ingresos = sum((producto.precio_venta_total if producto.precio_venta_total is not None else 0) 
                             for producto in self.inventario.lista_productos.values())
        print("Total de ingresos: ", total_ingresos)
    
 
    def calcular_costos(self):
        """Calcula el total de costos de los productos."""
        total_costos = sum((producto.precio_costo_total if producto.precio_costo_total is not None else 0)
                           for producto in self.inventario.lista_productos.values())
        print("Total de costos: ", total_costos)
    
  
    def calcular_ganancias(self):
        """Calcula las ganancias como la diferencia entre ingresos y costos."""
        total_ingresos = self.calcular_ingresos()
        total_costos = self.calcular_costos()
        total_ganancias = (total_ingresos if total_ingresos is not None else 0) - (total_costos if total_costos is not None else 0)
        print("Total de ganancias: ", total_ganancias)
    
    
    def calcular_margen_ganancias(self):
        """Calcula el margen de ganancias como un porcentaje."""
        total_ganancias = self.calcular_ganancias()
        total_ingresos = self.calcular_ingresos()
        if total_ingresos > 0 if total_ingresos is not None else False:
            margen_ganancias = (total_ganancias / total_ingresos) * 100
            print("Margen de ganancias: ", margen_ganancias, "%")
        else:
            print("Aún no hay margen de ganancias.")

  
    def calcular_inventario_promedio(self):
        stock_inicial = self.inventario.calcular_stock_inicial()
        stock_final = self.inventario.calcular_stock_final()
        
        # Calcular el inventario promedio
        inventario_promedio = (stock_inicial + stock_final) / 2
        print(f"Inventario promedio: {inventario_promedio}")






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
        if total_ingresos > 0 if total_ingresos is not None else 0:
            margen_ganancias = (total_ganancias / total_ingresos) * 100
            print("Margen de ganancias: ", margen_ganancias, "%")
        else:
            print("Aún no hay margen de ganancias.")

  
    def calcular_inventario_promedio(self):
        """Calcula el inventario promedio de todos los productos."""
        stock_inicial = self.inventario.calcular_stock_inicial()
        stock_final = self.inventario.calcular_stock_final()

        inventario_promedio = (stock_inicial + stock_final) / 2
        print(f"Inventario promedio: {inventario_promedio}")

    
    def calcular_rotacion(self):
        """Calcula el índice de rotación del inventario."""
        total_ingresos = self.calcular_ingresos()
        inventario_promedio = self.calcular_inventario_promedio()

        if inventario_promedio > 0:
            rotacion = total_ingresos / inventario_promedio
            print(f"El índice de rotación es: {rotacion}")
            return rotacion
        else:
            print("No se puede calcular el índice de rotación: inventario promedio es 0.")
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






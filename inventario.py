from producto import Producto
from datetime import datetime
from datetime import timedelta

class Inventario:
  
    def __init__(self):
        """Inicializa un diccionario vacío para almacenar los productos por su nombre."""
        self.lista_productos = {}
   
    def registrar_entrada(self, producto, mantener_fecha = False):
      
        """Registra la entrada de un producto al inventario.

        Si el producto ya existe (basado en su nombre), incrementa la cantidad.
        Si el producto no existe, lo agrega al diccionario.
      
        
        """

        producto.nombre = producto.nombre.lower()

        if producto.nombre in self.lista_productos:
            # Si el producto ya existe, actualiza la cantidad de unidades
            self.lista_productos[producto.nombre].fecha_actualizacion = datetime.now()
            self.lista_productos[producto.nombre].unidades += producto.unidades
            print(f"Producto '{producto.nombre}' ya existe. Unidades actualizadas a {self.lista_productos[producto.nombre].unidades}.")
        else:
            if not mantener_fecha:
                # Si no existe, lo agrega
                producto.fecha_ingreso = datetime.now()
                self.lista_productos[producto.nombre] = producto
                print(f"Producto '{producto.nombre}' agregado al inventario.")

   
    def registrar_salida(self, nombre, cantidad):
     
        """Registra la salida de un producto del inventario.

        Si el producto existe (basado en su nombre) y la cantidad es menor o igual a la cantidad disponible, disminuye la cantidad.
        Si la cantidad es mayor a la cantidad disponible, muestra un mensaje de error.
        Si el producto no existe, muestra un mensaje de error.
        """
      
        nombre = nombre.lower()
        if nombre in self.lista_productos:
            producto = self.lista_productos[nombre]
            producto.fecha_actualizacion = datetime.now()
            if cantidad <= producto.unidades:
                    producto.unidades -= cantidad
                    print(f"Se han retirado {cantidad} unidades del producto '{producto.nombre}'. Quedan {producto.unidades} unidades.")
            else:
                print(f"No hay suficientes unidades del producto '{producto.nombre}'. Solo hay {producto.unidades} disponibles.")
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")

    
 
    def buscar_producto(self, nombre):
   
        """
        Busca un producto en el inventario por su nombre.
        Si el producto existe, lo retorna; de lo contrario, retorna None.
     
        """
      
        nombre = nombre.lower()
        if nombre in self.lista_productos:
            producto = self.lista_productos[nombre]
            print(f"Producto '{producto.nombre}' encontrado.")
            print (f"Nombre: {producto.nombre}\n"
                    f"Precio por unidad: {producto.precio_unidad}\n"
                    f"Precio total: {producto.precio_total}\n"
                    f"Unidades: {producto.unidades}\n"
                    f"Fecha de Ingreso: {producto.fecha_ingreso}\n"
                    f"Fecha de actualización: {producto.fecha_actualizacion}\n"
                    f"Fecha de Vencimiento: {producto.fecha_vencimiento}\n")
            

            return self.lista_productos[nombre]
        return None
    


    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario por su nombre.
        Si el producto existe, lo elimina y retorna True; de lo contrario, retorna False.
        """
        nombre = nombre.lower()
        if nombre in self.lista_productos:
            producto_eliminado = self.lista_productos[nombre]
            del self.lista_productos[nombre]
            print(f"El producto '{producto_eliminado.nombre}' ha sido eliminado.")
            return True
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")
            return False
        

    def listar_productos(self):
        """Muestra la cantidad total de productos en el inventario."""
        print(f"La cantidad de productos en el inventario es: {len(self.lista_productos)}")

  
    def imprimir_productos(self):
        """Imprime los detalles de todos los productos en el inventario."""
        if not self.lista_productos:
            print("No hay productos en el inventario.")
            return

        for producto in self.lista_productos.values():
            print(producto.detalles())
    
  
    def proximo_a_vencer(self):
        """Imprime los productos que están próximos a vencer."""
        for producto in self.lista_productos.values():
                if datetime.now() <= producto.fecha_vencimiento <= datetime.now() + timedelta(days=30):
                    print(f"Producto '{producto.nombre}' próximo a vencer. Fecha de vencimiento: {producto.fecha_vencimiento}")
    
   
    def vencidos(self):
        """Imprime los productos que ya han vencido."""
        for producto in self.lista_productos.values():
            if producto.fecha_vencimiento < datetime.now():
                print(f"Producto '{producto.nombre}' vencido. Fecha de vencimiento: {producto.fecha_vencimiento}")



producto1 = Producto("Arroz", 5000, 100, "Diana", datetime(2023, 12, 31))
producto2 = Producto("Papa", 2000, 50, "La Rústica", datetime(2023, 12, 31))
producto3 = Producto("Leche", 3000, 150, "Alpina", datetime(2023, 12, 31))

inventario = Inventario()

# Agregar los productos al inventario
inventario.registrar_entrada(producto1)
inventario.registrar_entrada(producto2)
inventario.registrar_entrada(producto3)

inventario.registrar_salida("Arroz", 50)
#inventario.imprimir_productos()


inventario.buscar_producto("Arroz")

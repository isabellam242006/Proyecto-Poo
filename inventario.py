from producto import Producto
from datetime import datetime

class Inventario:
    def __init__(self):
        """Inicializa un diccionario vacío para almacenar los productos."""
        self.lista_productos = {}
   
    def registrar_entrada(self, producto):
        """Registra la entrada de un producto al inventario.
 
        Si el producto ya existe (basado en su ID), incrementa la cantidad.
        Si el producto no existe, lo agrega al diccionario.
        """
        producto.fecha_ingreso = datetime.now()

        if producto.id in self.lista_productos:
            print("El producto ya existe")
            self.lista_productos[producto.id].unidades += producto.unidades
        self.lista_productos[producto.id] = producto
        print(f"Producto {producto.nombre} agregado al inventario")

   
    def registrar_salida(self, producto, cantidad):
        """Registra la salida de un producto del inventario.
 
        Si el producto existe (basado en su ID) y la cantidad es menor o igual a la cantidad disponible, disminuye la cantidad.
        Si la cantidad es mayor a la cantidad disponible, muestra un mensaje de error.
        Si el producto no existe, muestra un mensaje de error.
        """

        if producto.id in self.lista_productos:
            if producto.fecha_ultima_actualizacion is None:
                producto.fecha_ultima_actualizacion = datetime.now()
            if cantidad <= self.lista_productos[producto.id].unidades:
                self.lista_productos[producto.id].unidades -= cantidad
                print(f"Se han retirado {cantidad} unidades del producto {self.lista_productos[producto.id].nombre}")
            else:
                print("No hay suficientes unidades del producto")
        else:
            print("El producto no existe")

   
    def buscar_producto(self, id):
        """
        Busca un producto en el inventario por su ID.
        Si el producto existe, lo retorna; de lo contrario, retorna None.
        """
        if id in self.lista_productos:
            return self.lista_productos[id]
        return None

   
    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.
        Si el producto existe, lo elimina y retorna True; de lo contrario, retorna False.
        """
        if id in self.lista_productos:
            producto_eliminado = self.lista_productos[id]
            del self.lista_productos[id]
            print (f"El producto {producto_eliminado.nombre} ha sido eliminado")
            return True
        else:
            print("El producto no existe")
            return False

   
   
    def actualizar_producto(self, producto):
        """
        Actualiza la información de un producto en el inventario.
        Si el producto existe, lo actualiza y retorna True; de lo contrario, retorna False.
        """

        if producto.id in self.lista_productos:
            self.lista_productos[producto.id] = producto
            return True
        return False

   
    def listar_productos(self):
        print("La cantidad de productos en el inventario es: ", len(self.lista_productos))

    
    def imprimir_productos(self):
        for producto in self.lista_productos.values():
            print(f"ID: {producto.id}\n"
              f"Nombre: {producto.nombre}\n"
              f"Precio por unidad: {producto.precio_unidad}\n"
              f"Precio total: {producto.precio_total}\n"
              f"Unidades: {producto.unidades}\n"
              f"Fecha de Ingreso: {producto.fecha_ingreso}\n"
              f"Fecha de actualización: {producto.fecha_actualización}\n"
              f"Fecha de Vencimiento: {producto.fecha_vencimiento}\n")
    


# Crear una instancia de Producto
producto1 = Producto("Arroz", 5000, 100, "Diana")
producto2 = Producto("Papa", 2000, 50, "La Rústica")
producto3 = Producto("Leche", 3000, 150, "Alpina")
producto4 = Producto("Cereal", 4000, 200, "Zucaritas")
producto5 = Producto("Pan", 1000, 300, "Bimbo")
producto6 = Producto("Huevos", 500, 100, "Kikes")
producto7 = Producto("Frijoles", 2000, 50, "Del Campo")
producto8 = Producto("Carne", 7000, 150, "Friogan")
producto9 = Producto("Pollo", 3000, 200, "Pimpollo")
producto10 = Producto("Pescado", 6000, 300, "Frimar")
producto11 = Producto("Queso", 4000, 100, "Colanta")
producto12 = Producto("Yogurt", 1500, 50, "Alpina")
producto13 = Producto("Mantequilla", 2000, 150, "Colanta")
producto14 = Producto("Aceite", 3000, 200, "Premier")
producto15 = Producto("Azucar", 1000, 300, "Incauca")
producto16 = Producto("Sal", 500, 100, "Refisal")
producto17 = Producto("Café", 2000, 50, "Juan Valdez")
producto18 = Producto("Té", 3000, 150, "Hindú")
producto19 = Producto("Agua", 500, 200, "Cristal")
producto20 = Producto("Gaseosa", 2000, 300, "Colombiana")
producto21 = Producto("Jugo", 1000, 100, "Hit")
producto22 = Producto("Miel", 5000, 50, "Apis")
producto23 = Producto("Harina", 2000, 100, "Doña Arepa")
producto24 = Producto("Chocolate", 3000, 150, "Sol")
producto25 = Producto("Cereal de Maíz", 4000, 200, "Corn Flakes")
producto26 = Producto("Galletas", 1000, 300, "Noel")
producto27 = Producto("Jabón", 2000, 100, "Dersa")
producto28 = Producto("Shampoo", 5000, 150, "Savital")
producto29 = Producto("Detergente", 3000, 200, "Fab")
producto30 = Producto("Pasta", 2000, 250, "Doria")


# Crear una instancia de Inventario
inventario = Inventario()

# Agregar los productos al inventario
inventario.registrar_entrada(producto1)
inventario.registrar_entrada(producto2)
inventario.registrar_entrada(producto3)
inventario.registrar_entrada(producto4)
inventario.registrar_entrada(producto5)
inventario.registrar_entrada(producto6)
inventario.registrar_entrada(producto7)
inventario.registrar_entrada(producto8)
inventario.registrar_entrada(producto9)
inventario.registrar_entrada(producto10)
inventario.registrar_entrada(producto11)
inventario.registrar_entrada(producto12)
inventario.registrar_entrada(producto13)
inventario.registrar_entrada(producto14)
inventario.registrar_entrada(producto15)
inventario.registrar_entrada(producto16)
inventario.registrar_entrada(producto17)
inventario.registrar_entrada(producto18)
inventario.registrar_entrada(producto19)
inventario.registrar_entrada(producto20)
inventario.registrar_entrada(producto21)
inventario.registrar_entrada(producto22)
inventario.registrar_entrada(producto23)
inventario.registrar_entrada(producto24)
inventario.registrar_entrada(producto25)
inventario.registrar_entrada(producto26)
inventario.registrar_entrada(producto27)
inventario.registrar_entrada(producto28)
inventario.registrar_entrada(producto29)
inventario.registrar_entrada(producto30)

inventario.registrar_salida(producto1, 50)
inventario.actualizar_producto(producto1)


#inventario.buscar_producto(producto1.id)
#inventario.eliminar_producto(producto2.id)
#inventario.actualizar_producto(producto3)
inventario.listar_productos()
inventario.imprimir_productos()
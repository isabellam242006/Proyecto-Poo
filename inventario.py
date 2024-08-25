from producto import Producto

class Inventario:
    def __init__(self):
        """Inicializa un diccionario vacío para almacenar los productos."""
        self.lista_productos = {}

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario.
        Si el producto ya existe (basado en su ID), incrementa la cantidad.
        Si el producto no existe, lo agrega al diccionario.
        """
        if producto.id in self.lista_productos:
            print("El producto ya existe")
            self.lista_productos[producto.id].cantidad += producto.cantidad
        self.lista_productos[producto.id] = producto
        print(f"Producto {producto.nombre} agregado al inventario")

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
            del self.lista_productos[id]
            return True
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
        return self.lista_productos.values()
    
    def imprimir_productos(self):
        for producto in self.lista_productos.values():
            print(f"ID: {producto.id}\n"
              f"Nombre: {producto.nombre}\n"
              f"Precio: {producto.precio}\n"
              f"Cantidad: {producto.cantidad}\n"
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
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)
inventario.agregar_producto(producto4)
inventario.agregar_producto(producto5)
inventario.agregar_producto(producto6)
inventario.agregar_producto(producto7)
inventario.agregar_producto(producto8)
inventario.agregar_producto(producto9)
inventario.agregar_producto(producto10)
inventario.agregar_producto(producto11)
inventario.agregar_producto(producto12)
inventario.agregar_producto(producto13)
inventario.agregar_producto(producto14)
inventario.agregar_producto(producto15)
inventario.agregar_producto(producto16)
inventario.agregar_producto(producto17)
inventario.agregar_producto(producto18)
inventario.agregar_producto(producto19)
inventario.agregar_producto(producto20)
inventario.agregar_producto(producto21)
inventario.agregar_producto(producto22)
inventario.agregar_producto(producto23)
inventario.agregar_producto(producto24)
inventario.agregar_producto(producto25)
inventario.agregar_producto(producto26)
inventario.agregar_producto(producto27)
inventario.agregar_producto(producto28)
inventario.agregar_producto(producto29)
inventario.agregar_producto(producto30)



# Actualizar un producto (si es necesario)
producto1_actualizado = Producto("Arroz Integral", 5500, 120, "Diana")
inventario.actualizar_producto(producto1_actualizado)

# Imprimir los IDs de los productos para verificar que no cambian
print(producto1.id)
print(producto2.id)

# Imprimir la lista de productos en el inventario
inventario.imprimir_productos()
inventario.listar_productos()

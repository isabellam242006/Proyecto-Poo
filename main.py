class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - {self.precio} - {self.cantidad} - {self.id}"
    
class Bodega:
    def __init__(self):
        self.lista_productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.lista_productos:
            print("El producto ya existe")
            self.productos[producto.id].cantidad += producto.cantidad
        self.lista_productos[producto.id] = producto

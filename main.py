import uuid
from datetime import datetime, timedelta
import random
from producto import Producto
from inventario import Inventario


def main():
    inventario = Inventario()

    while True:
        print("\nBIENVENIDO A TU SISTEMA DE INVENTARIO")
        print("=====================================")
        print("Qué deseas realizar?")
        print("1. Registrar entrada de un producto")
        print("2. Registrar salida de un producto")
        print("3. Buscar un producto")
        print("4. Eliminar un producto")
        print("5. Actualizar un producto")
        print("6. Listar productos")
        print("7. Imprimir productos")
        print("8. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        try:
            if opcion == "1":
                # Registrar entrada de un producto
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad en unidades de ingreso del producto: "))
                marca = input("Ingrese la marca del producto: ")
                
                # Crear el objeto Producto
                producto = Producto(nombre, precio, cantidad, marca)
                
                # Registrar la entrada del producto en el inventario
                inventario.registrar_entrada(producto)
                print(f"Producto '{nombre}' registrado exitosamente en el inventario.")
           
            elif opcion == "2":
                # Registrar salida de un producto
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad en unidades de salida del producto: "))
                
                # Registrar la salida
                inventario.registrar_salida(nombre, cantidad)

            elif opcion == "3":
                # Buscar un producto por su nombre
                nombre = input("Ingrese el nombre del producto que desea buscar: ")
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print(f"Nombre: {producto.nombre}\n"
                          f"Precio por unidad: {producto.precio_unidad}\n"
                          f"Precio total: {producto.precio_total}\n"
                          f"Unidades: {producto.unidades}\n"
                          f"Marca: {producto.marca}\n"
                          f"Fecha de Ingreso: {producto.fecha_ingreso}\n"
                          f"Fecha de actualización: {producto.fecha_ultima_actualizacion}\n"
                          f"Fecha de Vencimiento: {producto.fecha_vencimiento}\n")
                else:
                    print(f"El producto '{nombre}' no existe en el inventario.")

            elif opcion == "4":
                # Eliminar un producto por su nombre
                nombre = input("Ingrese el nombre del producto que desea eliminar: ")
                inventario.eliminar_producto(nombre)

            elif opcion == "5":
                # Actualizar la información de un producto
                nombre = input("Ingrese el nombre del producto que desea actualizar: ")
                producto = inventario.buscar_producto(nombre)
                if producto:
                    nuevo_nombre = input(f"Nombre actual ({producto.nombre}). Ingrese nuevo nombre: ") or producto.nombre
                    nuevo_precio = float(input(f"Precio actual ({producto.precio_unidad}). Ingrese nuevo precio: ") or producto.precio_unidad)
                    nuevas_unidades = int(input(f"Unidades actuales ({producto.unidades}). Ingrese nuevas unidades: ") or producto.unidades)
                    
                    producto.nombre = nuevo_nombre
                    producto.precio_unidad = nuevo_precio
                    producto.unidades = nuevas_unidades

                    # Actualizar en el inventario
                    inventario.actualizar_producto(producto)
                    print(f"Producto '{producto.nombre}' actualizado correctamente.")

            elif opcion == "6":
                # Listar la cantidad de productos en el inventario
                inventario.listar_productos()

            elif opcion == "7":
                # Imprimir los detalles de todos los productos
                inventario.imprimir_productos()

            elif opcion == "8":
                # Salir del sistema
                print("Saliendo del sistema de inventario.")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar los datos correctos.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
       
        continuar = input("\n¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() == "n":
            print("Saliendo del sistema de inventario.")
            break


if __name__ == "__main__":
    main()


            
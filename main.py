import uuid
from datetime import datetime, timedelta
import random
from producto import *
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
        print("5. Listar productos")
        print("6. Imprimir productos")
        print("7. Conocer productos vencidos o por vencer")
        print("8. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        try:
            if opcion == "1":
                
                print("1.Frutas y verduras")
                print("2.Congelados")
                print("3.Empaquetados")
                tipo_producto = input("¿Desea ingresar un tipo de producto en específico? s/n: ")

                
                if tipo_producto.lower() == "s":
                    tipo = input("Ingrese el número del tipo de producto que desea ingresar: ")

                    nombre = input("Ingrese el nombre del producto: ")
                    precio = float(input("Ingrese el precio del producto por unidad: "))
                    cantidad = int(input("Ingrese la cantidad en unidades de ingreso del producto: "))
                    marca = input("Ingrese la marca del producto: ")

                    try:
                        año = int(input("Ingrese el año de vencimiento (YYYY): "))
                        mes = int(input("Ingrese el mes de vencimiento (MM): "))
                        dia = int(input("Ingrese el día de vencimiento (DD): "))
                    
                    # Convertir el año, mes y día en un objeto datetime
                        fecha_vencimiento = datetime(año, mes, dia)
                    except ValueError:
                        print("Fecha inválida. Asegúrese de ingresar un año, mes y día válidos.")
              
                    
                    if tipo == "1":
                     estado_producto = input("Ingrese el estado del producto (fresco, podrido, etc.): ")
                     peso_total = float(input("Ingrese el peso total del producto en kg: "))
                     producto = FrutasYVerduras(nombre, precio, cantidad, marca, fecha_vencimiento, estado_producto, peso_total)

                     inventario.registrar_entrada(producto)
                     print(f"Producto '{nombre}' registrado exitosamente en el inventario.")
           

                    elif tipo_producto == "2":
                    # Congelados
                     temperatura = float(input("Ingrese la temperatura actual del producto: "))
                     producto = Congelados(nombre, precio, cantidad, marca, fecha_vencimiento, temperatura)

                     inventario.registrar_entrada(producto)
                     print(f"Producto '{nombre}' registrado exitosamente en el inventario.")
           
                    
                    elif tipo_producto == "3":
                    # Empaquetados
                     calidad_empaque = input("Ingrese la calidad del empaque: ")
                     peso_neto = float(input("Ingrese el peso neto del producto en kg: "))
                     producto = Empaquetados(nombre, precio, cantidad, marca, fecha_vencimiento, calidad_empaque, peso_neto)

                     inventario.registrar_entrada(producto)
                     print(f"Producto '{nombre}' registrado exitosamente en el inventario.")

           

                     
                    
                
                elif tipo_producto.lower() == "n":
                    nombre = input("Ingrese el nombre del producto: ")
                    precio = float(input("Ingrese el precio del producto por unidad: "))
                    cantidad = int(input("Ingrese la cantidad en unidades de ingreso del producto: "))
                    marca = input("Ingrese la marca del producto: ")

                    try:
                        año = int(input("Ingrese el año de vencimiento (YYYY): "))
                        mes = int(input("Ingrese el mes de vencimiento (MM): "))
                        dia = int(input("Ingrese el día de vencimiento (DD): "))
                    
                    # Convertir el año, mes y día en un objeto datetime
                        fecha_vencimiento = datetime(año, mes, dia)
                    except ValueError:
                        print("Fecha inválida. Asegúrese de ingresar un año, mes y día válidos.")

                    producto = Producto(nombre, precio, cantidad, marca, fecha_vencimiento)
                    
                    # Registrar la entrada del producto en el inventario
                    inventario.registrar_entrada(producto)
                    print(f"Producto '{nombre}' registrado exitosamente en el inventario.")
                 
                else:
                    # Si se introduce una opción incorrecta (ni "s" ni "n")
                     print("Opción inválida. Debe ingresar 's' o 'n'. Intente nuevamente.")
                     
                    
           
            
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
                # Listar la cantidad de productos en el inventario
                inventario.listar_productos()

            elif opcion == "6":
                # Imprimir los detalles de todos los productos
                inventario.imprimir_productos()
                inventario.vencidos()
                inventario.proximo_a_vencer()
              
            elif opcion == "7":
                     # Imprimir los productos vencidos o por vencer
                     inventario.vencidos()
                     inventario.proximo_a_vencer()

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


            
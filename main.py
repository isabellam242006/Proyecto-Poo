import uuid
from datetime import datetime, timedelta
import random
from producto import *
from inventario import Inventario
from archivo_json import guardar_inventario_json, cargar_inventario_json
from analisis_monetario import *


def main():
    #inventario = Inventario()

    inventario = cargar_inventario_json()

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
        print("8. Conocer análisis monetario")
        print("9. Salir")


        opcion = input("Ingrese el número de la opción que desea realizar: ")

        try:
            if opcion == "1":
                
                print("1.Frutas y verduras")
                print("2.Congelados")
                tipo_producto = input("¿Desea ingresar un tipo de producto en específico? s/n: ")

                
                if tipo_producto.lower() == "s":
                    tipo = input("Ingrese el número del tipo de producto que desea ingresar: ")

                    nombre = input("Ingrese el nombre del producto: ")
                    precio_costo = float(input("Ingrese el precio de costo del producto por unidad: "))
                    precio_venta = float(input("Ingrese el precio de venta del producto por unidad: "))
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
                        continue
              
                    
                    if tipo == "1":
                     estado_producto = input("Ingrese el estado del producto: ")
                     peso_total = float(input("Ingrese el peso neto del producto por unidad: "))
                     producto = FrutasYVerduras(nombre, precio_costo, precio_venta, cantidad, marca, fecha_vencimiento, estado_producto, peso_total)

                     inventario.registrar_entrada(producto)
                     print(f"Producto '{nombre}' registrado exitosamente en el inventario.")
           

                    elif tipo == "2":
                    # Congelados
                     temperatura = float(input("Ingrese la temperatura actual del producto en centígrados: "))
                     producto = Congelados(nombre, precio_costo, precio_venta, cantidad, marca, fecha_vencimiento, temperatura)

                     inventario.registrar_entrada(producto)
                     producto.calcular_temperatura_optima()
                     print(f"Producto '{nombre}' registrado exitosamente en el inventario.")
              
                    
                
                elif tipo_producto.lower() == "n":
                    nombre = input("Ingrese el nombre del producto: ")
                    precio_costo = float(input("Ingrese el precio de costo del producto por unidad: "))
                    precio_venta = float(input("Ingrese el precio de venta del producto por unidad: "))
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
                        continue

                    producto = Producto(nombre, precio_costo, precio_venta, cantidad, marca, fecha_vencimiento)
                    
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
                    print(producto.detalles())
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
                # Calcular el análisis monetario
                analisis = AnalisisMonetario(inventario)
                analisis.calcular_ingresos()
                analisis.calcular_costos()
                analisis.calcular_ganancias()
                analisis.calcular_margen_ganancias()
                analisis.calcular_inventario_promedio()

            elif opcion == "9":
                # Salir del sistema
                guardar_inventario_json(inventario)
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
            guardar_inventario_json(inventario)
            break


if __name__ == "__main__":
    main()


            
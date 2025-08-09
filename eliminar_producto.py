def eliminar_producto(nombre_producto):
    try:
        with open('inventario.txt', 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        encontrado = False
        with open('inventario.txt', 'w', encoding='utf-8') as archivo:
            for linea in lineas:
                partes = linea.strip().split(", ")
                # Comparar solo el nombre (columna 0)
                if partes[0].lower() != nombre_producto.lower():
                    archivo.write(linea)
                else:
                    encontrado = True  # Encontrado y no escrito = eliminado

        if encontrado:
            print(f"Producto '{nombre_producto}' eliminado exitosamente.")
        else:
            print(f"Producto '{nombre_producto}' no encontrado.")

    except FileNotFoundError:
        print("El archivo inventario.txt no existe.")
    except OSError as e:
        print(f"Error de entrada/salida: {e}")

def mostrar_inventario(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print("Contenido del inventario:")
            print(contenido)
    except FileNotFoundError:
        print(f"No se encontró el archivo '{ruta_archivo}'.")
    except OSError as e:
        print(f"Error de entrada/salida: {e}")

if __name__ == "__main__":
    print("Inventario sin Modificar\n")
    mostrar_inventario('inventario.txt')
    producto_a_eliminar = input("Ingrese el nombre del producto a eliminar: ")
    eliminar_producto(producto_a_eliminar)
    print("Inventario Modificado\n")
    mostrar_inventario('inventario.txt')

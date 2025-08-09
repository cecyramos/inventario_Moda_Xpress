def modificar_nombre(nombre_actual, nombre_nuevo):
    try:
        with open('inventario.txt', 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        encontrado = False
        with open('inventario.txt', 'w', encoding='utf-8') as archivo:
            for linea in lineas:
                partes = linea.strip().split(", ")
                if partes[0].lower() == nombre_actual.lower():
                    partes[0] = nombre_nuevo
                    archivo.write(", ".join(partes) + "\n")
                    encontrado = True
                else:
                    archivo.write(linea)

        if encontrado:
            print(f"Producto '{nombre_actual}' modificado a '{nombre_nuevo}' exitosamente.\n")
        else:
            print(f"Producto '{nombre_actual}' no encontrado.")

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
    actual = input("Ingrese el nombre del producto a modificar: ")
    nuevo = input("Ingrese el nuevo nombre del producto: ")
    modificar_nombre(actual, nuevo)
    print("Inventario Modificado\n")
    mostrar_inventario('inventario.txt')

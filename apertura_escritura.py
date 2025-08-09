# Apertura de archivo en modo escritura: Escribir datos de nuevos productos.
def apertura_escritura(archivo, contenido_original, contenido_modificado):
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            contenido_original = file.read()
            print("Contenido del archivo original:")
            print(contenido_original)

        with open(archivo, "w", encoding="utf-8") as file:
            file.write("Esta es una nueva lista de productos\n")
            file.write("Los precios han aumentado\n")
            file.write("Camiseta Azul, 20 USD, 50 unidades, M\n")
            file.write("Pantalón Negro, 30 USD, 30 unidades, L\n")
            file.write("Chaqueta Roja, 45 USD, 20 unidades, S\n")
            file.write("Zapatillas Deportivas, 65 USD, 10 unidades, 42\n")
            file.write("Gorra Blanca, 15 USD, 100 unidades, Talla Única\n")
            print("Archivo sobreescrito exitosamente.")

        with open(archivo, "r", encoding="utf-8") as file:
            contenido_modificado = file.read()
            print("\nContenido del archivo modificado:")
            print(contenido_modificado)

    except FileNotFoundError:
        print("El archivo no existe.")
    except IOError:
        print("Hubo un error al intentar leer o escribir en el archivo.")

if __name__ == "__main__":
    apertura_escritura("inventario.txt", "", "")
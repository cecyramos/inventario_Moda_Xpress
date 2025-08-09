# Apertura de archivo en modo lectura: Leer todo el inventario.
def abrir_archivo(archivo, contenido):
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            contenido = file.read()
            print("Contenido del archivo:")
            print(contenido)
            return contenido
    except FileNotFoundError:
        print("El archivo no existe.")
    except IOError:
        print("Hubo un error al intentar leer el archivo.")

if __name__ == "__main__":
    abrir_archivo("inventario.txt", "")
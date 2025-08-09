def cerrar_archivos(archivo):
    try:
        print("Abrir archivo: ", archivo)
        archivo = open(archivo, 'r', encoding='utf-8')
        archivo.close()
        print("Archivo cerrado.")
    except FileNotFoundError:
        print("El archivo inventario.txt no existe.")
    except OSError as e:
        print(f"Error de entrada/salida: {e}")

if __name__ == "__main__":
    cerrar_archivos('inventario.txt')

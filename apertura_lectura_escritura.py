def lectura_escritura(ruta_archivo):
    try:
        with open(ruta_archivo, "r+", encoding="utf-8") as archivo:
            # transforma el archivo en una lista
            contenido = archivo.readlines()
            print("contenido del archivo: ")
            # para poner el puntero en la primera linea
            archivo.seek(0)
            # imprime el contenido
            print(archivo.read())
            # idica la linea a modificar
            print("\nlinea a modificar: ", contenido[1])
            # modifica la linea
            contenido[1] ="Pantalón Negro, 30 USD, 15 unidades, L\n"
            # imprime la linea modificada
            print(contenido[1])
            archivo.seek(0)
            # sobreescribe el archivo con el nuevo contenido
            archivo.writelines(contenido)
            print("archivo modificado.")
            archivo.seek(0)
            # imprime el nuevo contenido
            print("contenido del archivo modficado: \n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no existe.")
    except IOError:
        print("Hubo un error al intentar leer el archivo.")


lectura_escritura("inventario.txt")
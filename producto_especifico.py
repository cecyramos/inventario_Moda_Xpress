def producto_especifico(ruta_archivo,producto):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if producto in linea:
                    print(linea)
                    return 
        print("El producto no se encuentra en el inventario.")        
    except FileNotFoundError:
        print("El archivo no existe.")
    except IOError:
        print("Hubo un error al intentar leer el archivo.")

producto_especifico("inventario_Moda_Xpress/inventario.txt","Camiseta Azul")
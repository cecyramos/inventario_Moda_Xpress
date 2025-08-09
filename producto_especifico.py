def producto_especifico(ruta_archivo,producto):
    try:
        #abre el archivo
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            #lee el archivo y lo guarda en una lista
            lineas = archivo.readlines()
            #recorre la lista
            for linea in lineas:
                #busca el producto en la linea
                if producto in linea:
                    print(linea)
                    return 
        #si no encuentra el producto        
        print("El producto no se encuentra en el inventario.")        
    except FileNotFoundError:
        print("El archivo no existe.")
    except IOError:
        print("Hubo un error al intentar leer el archivo.")

producto_especifico("inventario_Moda_Xpress/inventario.txt","Camiseta Azul")
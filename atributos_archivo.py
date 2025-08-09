import os as os
import datetime as datetime
def obtener_atributos_archivo(archivo):
    ruta_archivo = archivo  # Reemplaza con la ruta de tu archivo
    datos_archivo = os.stat(ruta_archivo)
    tamaño = datos_archivo.st_size  # Tamaño del archivo en bytes
    tiempo_modificacion = datos_archivo.st_mtime  # Tiempo de última modificación
    tiempo_creacion = datos_archivo.st_ctime  # Tiempo de creación (puede variar en sistemas operativos)

    # Formatea los tiempos en un formato legible
    tiempo_modificacion_legible = datetime.datetime.fromtimestamp(tiempo_modificacion).strftime('%Y-%m-%d %H:%M:%S')
    tiempo_creacion_legible = datetime.datetime.fromtimestamp(tiempo_creacion).strftime('%Y-%m-%d %H:%M:%S')

    print(f"Tamaño: {tamaño} bytes")
    print(f"Última modificación: {tiempo_modificacion_legible}")
    print(f"Creación: {tiempo_creacion_legible}")
    
obtener_atributos_archivo("inventario_Moda_Xpress/inventario.txt")
# Apertura de archivo en modo "append": Agregar productos sin eliminar los datos existentes.
with open("inventario.txt", "r", encoding="utf-8") as file:
    contenido = file.read()
    print("Contenido del archivo original:")
    print(contenido)

file = open("inventario.txt", "a", encoding="utf-8")
file.write("\nCalcetines Grises, 5 USD, 40 unidades, Talla Única")
file.write("\nBolso Negro, 35 USD, 20 unidades, Talla Únicaa")
file.write("\nShorts Negros, 20 USD, 35 unidades, Talla M")
file.close()

with open("inventario.txt", "r", encoding="utf-8") as file:
    contenido = file.read()
    print("")
    print("Contenido del archivo modificado:")
    print(contenido)
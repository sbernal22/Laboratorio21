def copiar_archivo_texto(origen, destino):
    with open(origen, 'r') as archivo_origen:
        contenido = archivo_origen.read()
    with open(destino, 'w') as archivo_destino:
        archivo_destino.write(contenido)
    print("Archivo de texto copiado")

with open("original.txt", "w") as f:
    f.write("Hola mundo")
copiar_archivo_texto("original.txt", "copia.txt")
print("\nContenido del archivo copiado:")
with open("copia.txt", "r") as f:
    print(f.read())
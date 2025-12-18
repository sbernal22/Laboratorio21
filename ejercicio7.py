def copiar_archivo_binario(origen, destino):
    with open(origen, 'rb') as archivo_origen:
        contenido = archivo_origen.read()
    with open(destino, 'wb') as archivo_destino:
        archivo_destino.write(contenido)
    print("Archivo binario copiado exitosamente")
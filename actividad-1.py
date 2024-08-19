from PIL import Image
print("ingrese la ruta de su imagen:")
img = input(str())
imagen = Image.open(img)
imagen.show()
resolucion = imagen.size

cantidadDePix = resolucion[0] * resolucion[1]
print(f"{'el tamaño de la imagen es:':<20} : {imagen.size}")
print(f"{'el formato de la imagen es:':<20}: {imagen.format}")
print (f"{'resolucion :':<20}: {resolucion[0] * resolucion[1]}")
print(f"{'cantidad de pixeles :':<20} : {cantidadDePix}")
print(f"{'ubicacion de la imagen:':<20}: {img}")

from PIL import Image

ruta = input("ingrese la ruta de la imagen:")
imagen = Image.open(ruta)
imagen.show()
nombreNuevo = "imagenNew.jpg"
imagen.save(nombreNuevo)
print(f"el nuevo nombre es:{nombreNuevo}")
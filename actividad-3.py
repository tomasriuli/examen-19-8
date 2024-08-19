from PIL import Image
print("ingrese la ruta de su imagen porfavor:")
img = input(str())
rotamiento = float(input("ingrese cual quiere que sea el rotamiento de la imagen en grados:"))
imagen = Image.open(img)
imagenrotada= imagen.rotate(rotamiento,expand = True)
imagenrotada.show()
Nombreinicial = img.split("/")[-1]
nom , ext = Nombreinicial.rsplit(".",1)
imagenrotada.save(Nombreinicial)
print(f"imagen se guardo como {Nombreinicial}")

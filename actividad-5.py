from PIL import Image
import os

ruta = input("ingresa la ruta de la imagen porfavor:")
Marcaruta = input("ingrese la ruta de la marca de agua:")
ubicacion = input("elige la ubicacion (superior izquierda,superior derecha,inferior derecha,inferior izquierda):").lower()
imagen = Image.open(ruta)
marca = Image.open(Marcaruta)
margen = 50
if ubicacion == "superior izquierda":
    posicion = (margen,margen)
elif ubicacion == "superior derecha":
    posicion=(imagen.width-marca.width-margen,margen)
elif ubicacion == "inferior izquierda":
    posicion = (margen,imagen.heigth-marca.heigth-margen)
else:
    posicion = (imagen.width-marca.width-margen,margen.heigth-marca.heigth-margen)
    
imagen.paste(marca,posicion,marca)
NomMarca = (f"marcada_{os.path.basename(ruta)}")
imagen.save(NomMarca)
Image.show()
print(f"imagen marcada guardada como{NomMarca}")
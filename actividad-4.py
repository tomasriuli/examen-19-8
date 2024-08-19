from  PIL import Image
import os
ruta = input("ingrese la ruta de la imagen porfavor:")
x = int(input("cordenadas x inicial:"))
y = int(input("cordenadas y inical:"))
ancho = int(input("ancho del recorte:"))
alto = int(input("alto del recorte:"))

try:
    imagen = Image.open(ruta)
    recorte = imagen.crop((x,y,x + ancho,y + alto))
    os.makedirs("recortes",exist_ok=True)
    recortesNew = len(os.listdir("recortes"))
    recorteX_png = f"recortes/recorte(recortesNew + 1).png"
    recorte.save(recorteX_png)
    print(f"recorte guardado como{recorteX_png}")
except Exception as e:
    print(f"error:{e}")
    
from PIL import Image
import numpy as np
Image.MAX_IMAGE_PIXELS = None

def crop(image_path):

    # coords and saved_location

    image_obj = Image.open(image_path)

    width, height = image_obj.size

    col = 0
    row = 0
    matriz = []
    coords = ()
    imgArr = list(image_obj.getdata())
    pxlCont = 0
    for px in imgArr:
        if (pxlCont-(width*row)) == width:
            row+=1
            col = 0

        if px == (0,0,0):
            data = {'width':col, 'height':row, 'pixel':pxlCont}
            matriz.append(data)
        pxlCont+=1
        col+=1

    matriz = sorted(matriz, key=lambda k: k['width'])
    left = (matriz[0]['width'])
    right = (matriz[len(matriz)-1]['width'])
    matriz = sorted(matriz, key=lambda k: k['height'])
    top = (matriz[0]['height'])
    bottom = (matriz[len(matriz)-1]['height'])
    cropped_image = image_obj.crop((left,top,right,bottom))
    cropped_image.save('firmaCrop.png')

crop('firma.png')
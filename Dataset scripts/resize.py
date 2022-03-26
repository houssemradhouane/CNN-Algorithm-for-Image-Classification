import PIL
import os
import os.path
from PIL import Image


path = r'./CPU cooler'
for file in os.listdir(path): 
    f_img = path+"/"+file
    img = Image.open(f_img)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize((256, 256)) #(width, height)
    img.save(f_img)
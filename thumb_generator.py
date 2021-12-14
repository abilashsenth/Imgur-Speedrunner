from PIL import Image
from resizeimage import resizeimage
import pyimgur
import os

# the variable: directory shall point to the folder containing images from which thumbnails should be extracted, and originals shall be compressed

directory = r'C:\Users\ADMIN\Desktop\scripts\conversion'


def make_thummbnail_jpeg(img, i):
        nameThumbx = "thumb"+str(i)+'.jpg'
        if(img.size[0]>400):
            basewidth = 400 
        else:
            basewidth = img.size[0]
        
        img = resizeimage.resize_width(img, basewidth)
        rgb_im = img.convert('RGB')
        rgb_im.save(nameThumbx)

def make_thummbnail_png(img, i):   
        nameThumb = "thumb"+str(i)+'.jpg'
        if(img.size[0]>400):
            basewidth = 400 
        else:
            basewidth = img.size[0]
        img = resizeimage.resize_width(img, basewidth)
        img.save(nameThumb)

def convertToPng():
    c = 1
    i=1
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            im  =Image.open(directory+ '\\' +filename)
            if im.mode != 'RGB':
                im = im.convert('RGB')
            make_thummbnail_jpeg(im,i)
            i+=1
            im = resizeimage.resize_width(im, im.size[0]-1)
            rgb_im = im.convert('RGB')
            name ='img'+str(c)+'.png'
            rgb_im.save(name)
            print(os.path.join(directory, filename))
            c+=1
            continue
        elif filename.endswith(".png"):
            im  =Image.open(directory+ '\\' +filename)
            if im.mode != 'RGB':
                im = im.convert('RGB')
            make_thummbnail_png(im, i)
            i+=1
            im = resizeimage.resize_width(im, im.size[0]-1)
            rgb_im = im.convert('RGB')
            name ='img'+str(c)+'.png'
            rgb_im.save(name)
            print(os.path.join(directory, filename))
            c+=1
            continue

        else:
            continue
    

convertToPng()






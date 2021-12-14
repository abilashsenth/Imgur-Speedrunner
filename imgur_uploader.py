from PIL import Image
from resizeimage import resizeimage
import pyimgur
import os
import sys
import re

# Please note that completed_dir shall point 
# to the directory where the images to be uploaded are present
# You can get your Imgur CLIENT_ID and CLIENT_SECRET from https://api.imgur.com/

completed_dir = r'C:\Users\ADMIN\Desktop\scripts\conversion\finished\upload'
CLIENT_ID = "clientID_goes_here"
CLIENT_SECRET = "clientSecret_goes_here"

printf = sys.stdout.write

alist = []
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def upload_to_imgur(PATH, name, alist=alist):
    im = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)
    uploaded_image = im.upload_image(PATH, title=name)
    print(uploaded_image.title)
    print(uploaded_image.link)
    print(uploaded_image.size)
    print(uploaded_image.type)
    alist.append(uploaded_image.link)
    #printlist()


def upload():
    list_dir = os.listdir(completed_dir)
    list_dir.sort(key=natural_keys)
    print(list_dir)
    for filename in list_dir:
        if filename.endswith(".png"):
            upload_to_imgur(completed_dir+ '\\' +filename, filename)
            continue
        else:
            continue

def upload_in_order():
    list_dir = os.listdir(completed_dir)
    list_dir.sort(key=natural_keys)
    print(list_dir)
    for filename in list_dir:
        if filename.endswith(".jpg"):
            upload_to_imgur(completed_dir+ '\\' +filename, filename)
            continue
        else:
            continue

def printlist():
    alist.reverse
    print(*alist, sep='","')


try:
    upload()
    printlist()
except Exception as e:
    print("exception has occured"+str(e))
    #printlist()
    

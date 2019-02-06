'''
import_images.py
    determine whether images are greyscale
    convert to greyscale if RGB
    file i/o to load images, matrix manipulation, standardization
'''

import PIL
import os
from skimage.io import imread_collection

dir_name = 'NeedleImages/'
imgs = []
greyscale = []

# creating a collection with the available images
col = imread_collection(os.path.join(dir_name, '*.jpg'))
# select one image for analysis
im = col[14]

print(type(im))
print(im.shape)

# create list of .jpg files in img directory
for root, dirs, files in os.walk(dir_name):
    for file in files:
        if file.endswith('.jpg'):
            imgs.append(file)

# create function to test whether images are greyscale
def is_grey_scale(img_path):
    im = PIL.Image.open(img_path).convert('RGB')
    w,h = im.size
    for i in range(w):
        for j in range(h):
            r,g,b = im.getpixel((i,j))
            if r != g != b:
                return False
    return True

# test set of images for greyscale
# for i in imgs:
#     img = os.path.join(dir_name, i)
#     greyscale.append(is_grey_scale(img))

# print(greyscale)
# print(len(greyscale))

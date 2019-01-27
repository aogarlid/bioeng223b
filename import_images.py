'''
import_images.py
    convert images to gray-scale from rgb
    file i/o to load images, matrix manipulation, standardization
'''

from skimage.color import rgb2gray
from skimage.io import imread_collection

# set NeedleImages collection path
col_dir = 'NeedleImages/*.jpg'
# creating a collection with the available images
col = imread_collection(col_dir)

im = col[1]
img = rgb2gray(im)




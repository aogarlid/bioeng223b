'''
import_images.py
    convert images to gray-scale from rgb
    file i/o to load images, matrix manipulation, standardization
'''

from skimage.color import rgb2gray
from skimage.io import imread_collection
from skimage import data

# set NeedleImages collection path
col_dir = 'NeedleImages/*.jpg'
# creating a collection with the available images
col = imread_collection(col_dir)

img = col[1]
img_gray = rgb2gray(img)




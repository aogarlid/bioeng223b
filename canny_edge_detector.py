

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

from skimage import feature

from skimage.color import rgb2gray
from skimage.io import imread_collection

# set NeedleImages collection path
col_dir = 'NeedleImages/*.jpg'
# creating a collection with the available images
col = imread_collection(col_dir)

img = col[1]
img_gray = rgb2gray(img)


# Compute the Canny filter for two values of sigma
edges1 = feature.canny(img_gray)
edges2 = feature.canny(img_gray, sigma=3)

# display results
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                                    sharex=True, sharey=True)

ax1.imshow(im, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('noisy image', fontsize=20)

ax2.imshow(edges1, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Canny filter, $\sigma=1$', fontsize=20)

ax3.imshow(edges2, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Canny filter, $\sigma=3$', fontsize=20)

fig.tight_layout()

plt.show()
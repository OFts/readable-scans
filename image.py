from glob import glob
import os
import skimage.io
from skimage import data
from skimage.color import rgb2gray
from skimage.filters import try_all_threshold, threshold_minimum, threshold_local
from skimage.transform import rescale, resize, downscale_local_mean
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

mylist = os.listdir("lc")

# print(mylist[0])
# gauss = gaussian(rgb2gray(skimage.io.imread("images/"+mylist[43])), sigma=1)
# skimage.io.show()
# skimage.io.imsave(os.path.dirname(__file__)+'/test/test.png', arr=binary_min)


def show_two(image,binary,thresh):
  fig, ax = plt.subplots(2, 2, figsize=(10, 10))

  ax[0, 0].imshow(image, cmap=plt.cm.gray)
  ax[0, 0].set_title('Original')

  ax[0, 1].hist(image.ravel(), bins=256)
  ax[0, 1].set_title('Histogram')

  ax[1, 0].imshow(binary, cmap=plt.cm.gray)
  ax[1, 0].set_title('Thresholded (min)')

  ax[1, 1].hist(image.ravel(), bins=256)
  ax[1, 1].axvline(thresh, color='r')

  for a in ax[:, 0]:
    a.axis('off')

def conv_local():
  image = rgb2gray(skimage.io.imread("images/"+mylist[109]))

  global_thresh = threshold_minimum(image)
  binary_global = ((image > global_thresh).astype(int)*255).astype(np.uint8)
  print(global_thresh)
  # print(np.shape(binary_global))

  block_size = 121
  local_thresh = threshold_local(image, block_size, offset=0.1)
  binary_local = ((image > local_thresh).astype(int)*255).astype(np.uint8)

  binary_local[0:block_size,0:block_size] = 0

  fig, axes = plt.subplots(ncols=3 , figsize=(7, 8))
  ax = axes.ravel()


  ax[0].imshow(image, cmap=plt.cm.gray)
  ax[0].set_title('Original')

  ax[1].imshow(binary_global, cmap=plt.cm.gray)
  ax[1].set_title('Global thresholding')

  ax[2].imshow(binary_local, cmap=plt.cm.gray)
  ax[2].set_title('Local thresholding')

  for a in ax:
    a.axis('off')

  # skimage.io.imshow(binary_global,cmap=plt.cm.gray)
  # show_two(image, binary_global, global_thresh)

  plt.show()

def conv_one():
  image = rgb2gray(skimage.io.imread("images/"+mylist[13]))
  thresh_min = threshold_minimum(image)
  binary_min = image > thresh_min

  binary_min = binary_min.astype(int)

  skimage.io.imshow(binary_min,cmap=plt.cm.gray)
  # skimage.io.imsave(os.path.dirname(__file__)+'/thresh/img'+str(1)+'.png', arr=(binary_min*255).astype(np.uint8))
  plt.show()

def conv_all():
  image = skimage.io.imread("lc/"+mylist[195])
    
  width = 1576
  height = int(width * image.shape[0] / image.shape[1])

  image_resized = resize(image, (height, width), anti_aliasing=True)

  skimage.io.imsave(os.path.dirname(__file__)+'/lc_local/img196.png', arr=image_resized)

  # c=1
  # for a in mylist:
  #   image = rgb2gray(skimage.io.imread("lc/"+a))
    
  #   width = 1576
  #   height = int(width * image.shape[0] / image.shape[1])

  #   image_resized = resize(image, (height, width), anti_aliasing=True)

  #   block_size = 121
  #   local_thresh = threshold_local(image_resized, block_size, offset=0.1)
  #   binary_local = ((image_resized > local_thresh).astype(int)*255).astype(np.uint8)

  #   skimage.io.imsave(os.path.dirname(__file__)+'/lc_local/img'+str(c)+'.png', arr=binary_local)
  #   print(str(c)+"/"+str(len(mylist)))
  #   c+=1

conv_all()


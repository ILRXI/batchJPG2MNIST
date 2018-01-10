#ILRXI batchJPEG to MNIST Converter#
import os
import numpy as np
from PIL import Image

SCRIPT_PATH = os.path.dirname(os.path.abspath( __file__ ))

arr = []
arr1 = []

#batchJPG
ilrxiic=2

for r in range(ilrxiic):

	img = Image.open('%s/%s.jpg' % (SCRIPT_PATH, str(r + 1))).convert('L')

	if img.size[0] != 28 or img.size[1] != 28:
		img = img.resize((28, 28))

	for i in range(28):
		for j in range(28):
			pixel = 1.0 - float(img.getpixel((j, i)))/255.0
			arr.append(pixel)

arr = np.array(arr)
arr1 = np.append(arr1,arr)
arr1 = np.array(arr1).reshape((ilrxiic, 784))

mnist = arr1
#ILRXI batchJPEG to MNIST Converter#

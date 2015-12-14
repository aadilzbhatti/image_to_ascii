import numpy as np
from PIL import Image, ImageOps
import sys

# open the image
image = Image.open(sys.argv[1])

# if specified, take in a width and height; otherwise create optimal aspect ratio
if len(sys.argv) == 4:
	size = (image.size[1] / image.size[0]) * int(sys.argv[3]), (image.size[0] / image.size[1]) * int(sys.argv[2])
else:
	size = (image.size[1] / image.size[0]) * 400, (image.size[0] / image.size[1]) * 900

# resize
image.thumbnail(size, Image.ANTIALIAS)
image = np.array(ImageOps.grayscale(image)).astype(np.float64)

# make every pixel either 0 or 1 depending on amount of color
image = np.around(image / 255)
np.savetxt('text.txt', image, fmt='%i', delimiter='')
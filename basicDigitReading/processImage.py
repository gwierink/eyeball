import cv2
import numpy as np
import sys

# Read in image name as argument 1
image_name = str(sys.argv[1])
img_stem = image_name.split('.')

# Create intermediate and final result names
im_sharpen = img_stem[0] + "-sharpen.png"
im_res = img_stem[0] + "-result.png"

#image = cv2.imread('meter02cropped.png')
image = cv2.imread(image_name)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(gray, -1, sharpen_kernel)

#cv2.imwrite('sharpen.png', sharpen)
cv2.imwrite(im_sharpen, sharpen)
sharpen = 255 - sharpen
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
dilate = cv2.dilate(sharpen, kernel, iterations=1)

result = 255 - dilate
#cv2.imwrite('result.png', result)
cv2.imwrite(im_res, result)
cv2.waitKey(0)

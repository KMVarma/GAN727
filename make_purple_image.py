import numpy as np
import cv2

# Create a blank 300x300 black image
image = np.zeros((512, 512, 3), np.uint8)
# Fill image with red color(set each pixel to red)
image[:] = (106, 31, 52)

cv2.imwrite('3_fixed.jpg', image)
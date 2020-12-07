import cv2

filename = "datasets/not_resized/5.jpg"

oriimage = cv2.imread(filename)

oldx,oldy = oriimage.shape[0], oriimage.shape[1]
min_dim = min([oldx,oldy])
x_start = int((oldx - min_dim) / 2)
y_start = int((oldy - min_dim) / 2)
crop_img = oriimage[0:min_dim,0:min_dim].copy()

newx,newy = 512,512

newimage = cv2.resize(crop_img,(newx,newy))

cv2.imwrite('datasets/photo2ghibli/TrainB/5.jpg', newimage)
import cv2 

img = cv2.imread("images/iu.jfif",1)
cvimg = cv2.rotate(img,cv2.ROTATE_180)

height, width, channel = img.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 23, 1)
dst = cv2.warpAffine(img, matrix, (width, height))

cv2.imshow("iu", dst)
cv2.waitKey(0) 

cv2.destroyAllWindows()
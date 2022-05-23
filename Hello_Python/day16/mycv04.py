import cv2 

img = cv2.imread("images/iu.jfif",1)
cvimg = cv2.rotate(img,cv2.ROTATE_180)

cv2.imshow("iu", cvimg)
cv2.waitKey(0) 

cv2.destroyAllWindows()
import cv2 

img = cv2.imread("images/iu.jfif",1)
crop_img = img[50:150,20:200]

cv2.imshow("iu", img)
cv2.imshow("iu", crop_img)
cv2.waitKey(0) 

cv2.destroyAllWindows()
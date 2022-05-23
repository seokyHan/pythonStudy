import cv2 

img = cv2.imread("images/iu.jfif",1)
crop_img = img[20:200,10:200]
gray_img = cv2.cvtColor(crop_img,cv2.COLOR_RGB2GRAY)

height, width, channel = img.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 23, 1)
dst = cv2.warpAffine(gray_img, matrix, (width, height))


cv2.imshow("iu", dst)

cv2.imwrite('images/iu2.jpg',dst)
cv2.waitKey(0) 

cv2.destroyAllWindows()
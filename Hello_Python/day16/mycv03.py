import cv2 

img = cv2.imread("images/r.png",1)
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
print(img) 


cv2.imshow("iu", gray_img)
cv2.waitKey(0) 

cv2.destroyAllWindows()
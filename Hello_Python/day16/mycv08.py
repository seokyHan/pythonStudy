import cv2 

img = cv2.imread("images/iu.jfif",1)
print(img)

cv2.imshow("iu", img)
cv2.imwrite('images/iuiu.png',img)

cv2.waitKey(0) 
cv2.destroyAllWindows()
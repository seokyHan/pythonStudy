import cv2 

img = cv2.imread("images/r.png",1)
print(img)

cv2.imshow("iu", img)
cv2.waitKey(0) 

cv2.destroyAllWindows()
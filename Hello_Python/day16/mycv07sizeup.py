import cv2 
from scipy.ndimage import interpolation

img = cv2.imread("images/iu.jfif",1)
dst = cv2.resize(img,dsize=(640,480),interpolation=cv2.INTER_AREA)

cv2.imshow("iu", dst)

cv2.waitKey(0) 

cv2.destroyAllWindows()
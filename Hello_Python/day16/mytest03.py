import cv2 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread("images/iu.jfif",1)
img2 = cv2.imread("images/pangsu.png",1)

# 이미지 전처리
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 찾기
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.resize(img2,dsize=(200,200),interpolation=cv2.INTER_AREA)
    # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# 결과 출력
cv2.imshow('image', img)

key = cv2.waitKey(0)
cv2.destroyAllWindows()

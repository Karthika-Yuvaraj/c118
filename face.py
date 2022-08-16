import cv2

img = cv2.imread("boy.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face = face_cascade.detectMultiScale(gray)
print(len(face))

for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),10)
    crop = img[y:y+h,x:x+w]
    cv2.imwrite("crop.jpg",crop)

cv2.imshow("faceDetecor",img)
cv2.waitKey(0)
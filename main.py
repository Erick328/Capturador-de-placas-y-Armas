
import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
casific=cv2.CascadeClassifier('cascade.xml')
while True:
	ret,frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	toy=casific.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=10)
	for (x,y,w,h) in toy:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		cv2.putText(frame, 'Arma',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
	cv2.imshow('Detector de Armas',frame)
	if cv2.waitKey(1)==27:
		break
cap.release()
cv2.destroyAllWindows()



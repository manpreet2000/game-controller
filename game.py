import cv2
import numpy as np
import datetime
import time
from pymouse import PyMouse


def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)

    return resized

cap = cv2.VideoCapture(0)

m = PyMouse()

last_click = datetime.datetime.now()

while True:
	ret, frame = cap.read()

	frame = cv2.flip(frame, 1)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([139, 65, 121])
	upper_blue = np.array([164, 88, 176])
	mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

	lower_yellow = np.array([16, 101, 146])
	upper_yellow = np.array([179, 255, 255])
	mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

	contoursYellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for c in contoursYellow :
		if cv2.contourArea(c) <= 20 :
			continue
		x, y, _, _ = cv2.boundingRect(c)
		m.move(x+200, y+200)
		cv2.drawContours(frame, contoursYellow, -1, (0, 255, 0), 3)

	contoursBlue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for c in contoursBlue :
		if cv2.contourArea(c) <= 6 :
			continue
		now = datetime.datetime.now()
		diff = now - last_click
		if diff.total_seconds() > 0.5 :
			last_click = datetime.datetime.now()
			cv2.drawContours(frame, contoursBlue, -1, (0, 255, 0), 3)
			x, y = m.position()
			m.click(x, y, 1)
	
	frame = image_resize(frame, width = 700)  
	cv2.imshow("frame", frame)
	
	key = cv2.waitKey(1)
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()
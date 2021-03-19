import numpy as np
import cv2
from utils.recorder import Recorder
import os 


recorder = Recorder()
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)

filename = os.path.join(os.path.dirname(__file__), '../benchmarks/video.highres.avi')


recording = False

while(capture.isOpened()):
	ret, frame = capture.read()
	if ret==True:
	
		cv2.imshow('frame',frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'):
			break
		elif key == ord("r"):
			if not recording:
				recorder.start(frame, filename)
				recording = True
			else:
				recorder.stop()
				recording = False

		if recording:
			recorder.record(frame)
	else:
		break

# Release everything if job is finished
capture.release()
cv2.destroyAllWindows()
recorder.stop()
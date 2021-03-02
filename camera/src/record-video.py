from imutils.video import VideoStream, FPS
import cv2
import os 
import time

video = None

vs = None 
if os.uname()[4][:3] == 'arm':
	vs = VideoStream(usePiCamera=0).start()
else:
	vs = VideoStream(src=1).start()

# allow the camera to warmup
time.sleep(0.1)

for x in range(1000):
  frame = vs.read()
  (h, w) = frame.shape[:2]

  if video == None:
    video = cv2.VideoWriter('./video.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (w, h))

  video.write(frame)

video.release()

# import picamera

# with picamera.PiCamera() as camera:
#     camera.resolution = (640, 480)
#     camera.start_recording('my_video.h264')
#     camera.wait_recording(60)
#     camera.stop_recording()

# import the necessary packages
# from picamera.array import PiRGBArray
# from picamera import PiCamera
# import time
# import cv2
# import os
# import io
# from utils.recorder import Recorder

# recorder = Recorder()
resolution = (1920, 1088)

# # initialize the camera and grab a reference to the raw camera capture
# camera = PiCamera()
# camera.resolution = resolution
# camera.framerate = 32
# rawCapture = PiRGBArray(camera,  size=resolution)
# stream = io.BytesIO()

# # allow the camera to warmup
# time.sleep(0.1)

# counter = 0

# # capture frames from the camera
# for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
# 	# grab the raw NumPy array representing the image, then initialize the timestamp
# 	# and occupied/unoccupied text
# 	image = frame.array
# 	recorder.record(image, os.path.join(os.path.dirname(__file__), '../video.highres.avi'))

# 	counter += 1 
# 	if counter == 1000:
# 		recorder.stop()
# 		break


import picamera

with picamera.PiCamera() as camera:
	camera.resolution = resolution
	camera.start_recording('video.h264')
	camera.wait_recording(60)
	camera.stop_recording()


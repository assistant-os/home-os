import picamera

resolution = (1920, 1088)

with picamera.PiCamera() as camera:
	camera.resolution = resolution
	camera.start_recording('video.h264')
	camera.wait_recording(60)
	camera.stop_recording()


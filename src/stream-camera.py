from imutils.video import VideoStream, FPS
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import imutils
import time
import cv2
import os
import numpy as np 

from utils.benchmark import Benchmark
from utils.recorder import Recorder

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
globalFrame = None
lock = threading.Lock()
recorder = Recorder()
isRecording = False
# initialize a flask object
app = Flask(__name__)
# initialize the video stream and allow the camera sensor to

benchmark = Benchmark()

video = None 
if os.uname()[4][:3] == 'arm':
	video = VideoStream(usePiCamera=0, resolution=(1920,1080)).start()
else:
	video = VideoStream(src=1, resolution=(1920,1080)).start()


# warmup
time.sleep(2.0)

@app.route("/")
def index():
	# return the rendered template
	return render_template("index.html")

def compute_image(frameCount, rotate):
	# grab global references to the video stream, output frame, and
	# lock variables
	global video, globalFrame, lock

	# loop over frames from the video stream
	while True:
		# time.sleep(2)
		# read the next frame from the video stream, resize it,
		# convert the frame to grayscale, and blur it
		frame = video.read()

		benchmark.pre()
		frame = np.array(np.rot90(frame, k=2))
		benchmark.post()
		globalFrame = frame

def record_image():
	global recorder
	while True:
		if isRecording:
			recorder.record(globalFrame)

def generate():
	# grab global references to the output frame and lock variables
	global globalFrame, lock
	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if globalFrame is None:
				continue
			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", globalFrame)
			# ensure the frame was successfully encoded
			if not flag:
				continue
		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

@app.route("/save", methods=['POST'])
def save():
	cv2.imwrite('image.jpg', globalFrame)
	# return the response generated along with the specific media
	# type (mime type)
	return Response("{}",
				status=200,
				mimetype='application/json')

@app.route("/record", methods=['POST'])
def record():
	global isRecording, recorder, globalFrame
	if isRecording:
		isRecording = False
		recorder.stop()
	else:
		recorder.start(globalFrame, os.path.join(os.path.dirname(__file__), '../datasets/video.recorded.avi'))
		isRecording = True
	return Response("{}",
				status=200,
				mimetype='application/json')

# check to see if this is the main thread of execution
if __name__ == '__main__':
	# construct the argument parser and parse command line arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("--host", type=str, default='0.0.0.0',
		help="ip address of the device")
	ap.add_argument("-o", "--port", type=int,default=8080,
		help="ephemeral port number of the server (1024 to 65535)")
	ap.add_argument("--rotate", type=int, default=180,
		help="angle of rotation of the image")
	ap.add_argument("-f", "--frame-count", type=int, default=32,
		help="# of frames used to construct the background model")
	ap.add_argument('-c', '--confidence', type=float, default=0.5,
								help='minimum probability to filter weak detections')
	args = vars(ap.parse_args())
	# start a thread that will perform motion detection
	t = threading.Thread(target=compute_image, args=(
		args["frame_count"],args["rotate"]))
	t.daemon = True
	t.start()
	t2 = threading.Thread(target=record_image)
	t2.daemon = True
	t2.start()
	# start the flask app
	app.run(host=args["host"], port=args["port"], debug=True,
		threaded=True, use_reloader=False)
# release the video stream pointer
video.stop()
benchmark.stats()

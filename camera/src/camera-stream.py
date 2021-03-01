from imutils.video import VideoStream
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

dirname = os.path.dirname(__file__)

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(
		os.path.join(dirname, '../models/MobileNetSSD_deploy.prototxt'),
		os.path.join(dirname, '../models/MobileNetSSD_deploy.caffemodel'))

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

RED = (255, 0, 0)

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
globalFrame = None
lock = threading.Lock()
# initialize a flask object
app = Flask(__name__)
# initialize the video stream and allow the camera sensor to
# warmup
vs = VideoStream(usePiCamera=0).start()
# vs = VideoStream(src=1).start()

time.sleep(2.0)

def mat2gray(img):
		A = np.double(img)
		out = np.zeros(A.shape, np.double)
		normalized = cv2.normalize(A, out, 1.0, 0.0, cv2.NORM_MINMAX)
		return out

 # Add noise to the image


def random_noise(image, mode='gaussian', seed=None, clip=True, **kwargs):
		image = mat2gray(image)

		mode = mode.lower()
		if image.min() < 0:
				low_clip = -1
		else:
				low_clip = 0
		if seed is not None:
				np.random.seed(seed=seed)

		if mode == 'gaussian':
				noise = np.random.normal(kwargs['mean'], kwargs['var'] ** 0.5,
																 image.shape)
				out = image + noise
		if clip:
				out = np.clip(out, low_clip, 1.0)

		return out



@app.route("/")
def index():
	# return the rendered template
	return render_template("index.html")

def detect_motion(frameCount, rotate):
	# grab global references to the video stream, output frame, and
	# lock variables
	global vs, globalFrame, lock

	# loop over frames from the video stream
	while True:
		# read the next frame from the video stream, resize it,
		# convert the frame to grayscale, and blur it
		frame = vs.read()

		frame = np.array(np.rot90(frame, k=2))
		frame = imutils.resize(frame, width=512)

		(h, w) = frame.shape[:2]
		blob = cv2.dnn.blobFromImage(cv2.resize(frame, (512, 512)), 0.007843, (512, 512), 127.5)

		# pass the blob through the network and obtain the detections and predictions
		net.setInput(blob)
		detections = net.forward()

		nbPerson = 0
		confidences = []

		# loop over the detections
		for i in np.arange(0, detections.shape[2]):
				# extract the confidence (i.e., probability) associated with
				# the prediction
				confidence = detections[0, 0, i, 2]

				# filter out weak detections by ensuring the `confidence` is
				# greater than the minimum confidence
				if confidence > args["confidence"]:
						# extract the index of the class label from the
						# `detections`, then compute the (x, y)-coordinates of
						# the bounding box for the object
						idx = int(detections[0, 0, i, 1])
						box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
						(startX, startY, endX, endY) = box.astype("int")

						if CLASSES[idx] == "person":
								cv2.rectangle(frame, (startX, startY), (endX, endY),
															RED, 2)
								nbPerson += 1
								label = "{:.2f}%".format(confidence * 100)
								y = startY - 15 if startY - 15 > 15 else startY + 15
								cv2.putText(frame, label, (startX, y),
														cv2.FONT_HERSHEY_SIMPLEX, 0.5, RED, 2)

		label = "{}".format(nbPerson)
		cv2.putText(frame, label, (10, 20),
								cv2.FONT_HERSHEY_SIMPLEX, 0.5, RED, 2)

		globalFrame = frame

		# grab the current timestamp and draw it on the frame
		timestamp = datetime.datetime.now()
		cv2.putText(frame, timestamp.strftime(
			"%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

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
	print("save")
	cv2.imwrite('image.jpg', frame)
	# return the response generated along with the specific media
	# type (mime type)
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
	t = threading.Thread(target=detect_motion, args=(
		args["frame_count"],args["rotate"]))
	t.daemon = True
	t.start()
	# start the flask app
	app.run(host=args["host"], port=args["port"], debug=True,
		threaded=True, use_reloader=False)
# release the video stream pointer
vs.stop()
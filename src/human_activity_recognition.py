import numpy as np
import argparse
import imutils
import sys
import cv2
from utils.recorder import Recorder
import os 
from detectors.get_path import getPath

ap = argparse.ArgumentParser()
ap.add_argument("--video", type=str, default="",
	help="optional path to video file")
args = vars(ap.parse_args())

recorder = Recorder()

labelsPath = getPath("kinetics-400/action_recognition_kinetics.txt")
CLASSES = open(labelsPath).read().strip().split("\n")
SAMPLE_DURATION = 16
SAMPLE_SIZE = 112

print("[INFO] loading human activity recognition model...")
net = cv2.dnn.readNet(getPath("kinetics-400/resnet-34_kinetics.onnx"))

print("[INFO] accessing video stream...")
video = cv2.VideoCapture(args["video"] if args["video"] else 1)

while True:
	
	frames = []

	
	for i in range(0, SAMPLE_DURATION):
		(grabbed, frame) = video.read()

		
		if not grabbed:
			print("[INFO] no frame read from stream - exiting")
			sys.exit(0)

		
		frame = imutils.resize(frame, width=400)
		frames.append(frame)

	blob = cv2.dnn.blobFromImages(frames, 1.0,
		(SAMPLE_SIZE, SAMPLE_SIZE), (114.7748, 107.7354, 99.4750),
		swapRB=True, crop=True)
	blob = np.transpose(blob, (1, 0, 2, 3))
	blob = np.expand_dims(blob, axis=0)

	
	net.setInput(blob)
	outputs = net.forward()
	label = CLASSES[np.argmax(outputs)]

	for frame in frames:
		cv2.rectangle(frame, (0, 0), (300, 40), (0, 0, 0), -1)
		cv2.putText(frame, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
			0.8, (255, 255, 255), 2)

		recorder.record(frame, os.path.join(os.path.dirname(__file__), '../benchmarks/video.kinetics.avi'))

		cv2.imshow("Activity Recognition", frame)
		key = cv2.waitKey(1) & 0xFF

		if key == ord("q"):
			recorder.stop()
			cv2.destroyAllWindows()
			break
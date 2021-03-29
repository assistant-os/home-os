# USAGE
# python human_activity_reco.py --model resnet-34_kinetics.onnx --classes action_recognition_kinetics.txt --input example_activities.mp4
# python human_activity_reco.py --model resnet-34_kinetics.onnx --classes action_recognition_kinetics.txt

import numpy as np
import argparse
import imutils
import sys
import cv2
from utils.recorder import Recorder
import os 

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained human activity recognition model")
ap.add_argument("-c", "--classes", required=True,
	help="path to class labels file")
ap.add_argument("-i", "--input", type=str, default="",
	help="optional path to video file")
args = vars(ap.parse_args())

recorder = Recorder()

CLASSES = open(args["classes"]).read().strip().split("\n")
SAMPLE_DURATION = 16
SAMPLE_SIZE = 112

print("[INFO] loading human activity recognition model...")
net = cv2.dnn.readNet(args["model"])

print("[INFO] accessing video stream...")
video = cv2.VideoCapture(args["input"] if args["input"] else 0)

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
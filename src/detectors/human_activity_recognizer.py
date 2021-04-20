import os
import cv2
import imutils
import numpy as np 
from .get_path import getPath

SAMPLE_DURATION = 16
SAMPLE_SIZE = 112

class Detector:

		def __init__(self):
				labelsPath = getPath("kinetics-400/action_recognition_kinetics.txt")
				self.CLASSES = open(labelsPath).read().strip().split("\n")
				print("[INFO] loading model...")
				self.net = cv2.dnn.readNet(getPath("kinetics-400/resnet-34_kinetics.onnx"))
				self.frames = []
		
		def detect(self, frame, confidenceRequired=0.5):

				frame = imutils.resize(frame, width=400)
				self.frames.append(frame)

				if len(self.frames) < SAMPLE_DURATION:
					return frame

				self.frames.pop(0)

				blob = cv2.dnn.blobFromImages(self.frames, 1.0,
					(SAMPLE_SIZE, SAMPLE_SIZE), (114.7748, 107.7354, 99.4750),
					swapRB=True, crop=True)
				blob = np.transpose(blob, (1, 0, 2, 3))
				blob = np.expand_dims(blob, axis=0)

				self.net.setInput(blob)
				outputs = self.net.forward()
				label = self.CLASSES[np.argmax(outputs)]

				cv2.rectangle(frame, (0, 0), (300, 40), (0, 0, 0), -1)
				cv2.putText(frame, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
					0.8, (255, 255, 255), 2)
				
				return frame
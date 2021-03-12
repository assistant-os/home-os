import os
import cv2
import imutils
import numpy as np 

dirname = os.path.dirname(__file__)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
							"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
							"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
							"sofa", "train", "tvmonitor"]

RED = (255, 0, 0)

class PersonDetector:

	def __init__(self):
		print("[INFO] loading model...")
		self.net = cv2.dnn.readNetFromCaffe(
				os.path.join(dirname, '../../models/MobileNetSSD/MobileNetSSD_deploy.prototxt'),
				os.path.join(dirname, '../../models/MobileNetSSD/MobileNetSSD_deploy.caffemodel'))

	
	def detect(self, frame, confidenceRequired):
		frame = imutils.resize(frame, width=512)
		(h, w) = frame.shape[:2]
		blob = cv2.dnn.blobFromImage(cv2.resize(frame, (512, 512)), 0.007843, (512, 512), 127.5)

		# pass the blob through the network and obtain the detections and predictions
		self.net.setInput(blob)
		detections = self.net.forward()

		nbPerson = 0
		confidences = []

		# loop over the detections
		for i in np.arange(0, detections.shape[2]):
			# extract the confidence (i.e., probability) associated with
			# the prediction
			confidence = detections[0, 0, i, 2]

			# filter out weak detections by ensuring the `confidence` is
			# greater than the minimum confidence
			if confidence > confidenceRequired:
				# extract the index of the class label from the
				# `detections`, then compute the (x, y)-coordinates of
				# the bounding box for the object
				idx = int(detections[0, 0, i, 1])
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")

				if CLASSES[idx] == "person":
					cv2.rectangle(frame, (startX, startY), (endX, endY), RED, 2)
					nbPerson += 1
					label = "{:.2f}%".format(confidence * 100)
					y = startY - 15 if startY - 15 > 15 else startY + 15
					cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, RED, 2)


			label = "{}".format(nbPerson)
			cv2.putText(frame, label, (10, 20),
									cv2.FONT_HERSHEY_SIMPLEX, 0.5, RED, 2)
		
		return frame
import os
import cv2
import imutils
import numpy as np 

# https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/

currentDirname = os.path.dirname(__file__)

yoloDirname = os.path.join(currentDirname, '../../models/yolo-coco/')

# [List of classes](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

threshold = 0.3

class PersonDetector:

	def __init__(self):
		labelsPath = os.path.join(yoloDirname,"coco.names")
		self.LABELS = open(labelsPath).read().strip().split("\n")
		np.random.seed(42)
		self.COLORS = np.random.randint(0, 255, size=(len(self.LABELS), 3),
			dtype="uint8")


		# derive the paths to the YOLO weights and model configuration
		weightsPath = os.path.join(yoloDirname, "yolov3.weights")
		configPath = os.path.join(yoloDirname, "yolov3.cfg")
		# load our YOLO object detector trained on COCO dataset (80 classes)
		print("[INFO] loading YOLO from disk...")
		self.net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

	
	def detect(self, frame, confidenceRequired):
		frame = imutils.resize(frame, width=512)
		(H, W) = frame.shape[:2]

		ln = self.net.getLayerNames()
		ln = [ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

		blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)

		self.net.setInput(blob)
		layerOutputs = self.net.forward(ln)

		boxes = []
		confidences = []
		classIDs = []

		# loop over each of the layer outputs
		for output in layerOutputs:
			# loop over each of the detections
			for detection in output:
				# extract the class ID and confidence (i.e., probability) of
				# the current object detection
				scores = detection[5:]
				classID = np.argmax(scores)
				confidence = scores[classID]
				# filter out weak predictions by ensuring the detected
				# probability is greater than the minimum probability
				if confidence > confidenceRequired:
					# scale the bounding box coordinates back relative to the
					# size of the image, keeping in mind that YOLO actually
					# returns the center (x, y)-coordinates of the bounding
					# box followed by the boxes' width and height
					box = detection[0:4] * np.array([W, H, W, H])
					(centerX, centerY, width, height) = box.astype("int")
					# use the center (x, y)-coordinates to derive the top and
					# and left corner of the bounding box
					x = int(centerX - (width / 2))
					y = int(centerY - (height / 2))
					# update our list of bounding box coordinates, confidences,
					# and class IDs
					boxes.append([x, y, int(width), int(height)])
					confidences.append(float(confidence))
					classIDs.append(classID)

		# apply non-maxima suppression to suppress weak, overlapping bounding
		# boxes
		idxs = cv2.dnn.NMSBoxes(boxes, confidences, confidenceRequired,
			threshold)

			# ensure at least one detection exists
		if len(idxs) > 0:
			# loop over the indexes we are keeping
			for i in idxs.flatten():
				# extract the bounding box coordinates
				(x, y) = (boxes[i][0], boxes[i][1])
				(w, h) = (boxes[i][2], boxes[i][3])
				# draw a bounding box rectangle and label on the image
				color = [int(c) for c in self.COLORS[classIDs[i]]]
				cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
				text = "{}: {:.4f}".format(self.LABELS[classIDs[i]], confidences[i])
				cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
					0.5, color, 2)

		return frame
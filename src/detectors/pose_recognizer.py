import os
import cv2
import imutils
import numpy as np 
from .get_path import getPath

BODY_PARTS = { "Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
									 "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
									 "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
									 "Background": 15 }

POSE_PAIRS = [ ["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
									 ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
									 ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
									 ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"] ]


class Detector:

		def __init__(self):
				print("[INFO] loading model...")
				self.net = cv2.dnn.readNetFromCaffe(getPath('pose/mpi/pose_iter_160000.prototxt'), getPath('pose/mpi/pose_iter_160000.caffemodel'))
		
		def detect(self, frame, confidenceRequired=0.5):
				(height, width) = frame.shape[:2]

				blob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (width, height), (0, 0, 0), swapRB=False, crop=False)

				# Set the prepared object as the input blob of the network
				self.net.setInput(blob)

				output = self.net.forward()
				threshold = 0.5

				H = output.shape[2]
				W = output.shape[3]
				# Empty list to store the detected keypoints
				points = []
				for i in range(output.shape[1]):
						# confidence map of corresponding body's part.
						probMap = output[0, i, :, :]

						# Find global maxima of the probMap.
						minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

						# Scale the point to fit on the original image
						x = (width * point[0]) / W
						y = (height * point[1]) / H

						if prob > threshold :
								cv2.circle(frame, (int(x), int(y)), 2, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
								# cv2.putText(frame, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 3, lineType=cv2.LINE_AA)

								# Add the point to the list if the probability is greater than the threshold
								points.append((int(x), int(y)))
						else :
								points.append(None)

				for pair in POSE_PAIRS:
						partA = BODY_PARTS[pair[0]]
						partB = BODY_PARTS[pair[1]]

						if points[partA] and points[partB]:
								cv2.line(frame, points[partA], points[partB], (0, 255, 0), 3)
				
				return frame
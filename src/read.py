import cv2
import os
import imutils
import argparse

from detectors.pose_recognizer import Detector as PoseDetector
from detectors.person_detector_yolo import Detector as YoloDetector
from detectors.person_detector_ssd import Detector as SsdDetector

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default="",
	help="optional path to video file")
args = vars(ap.parse_args())


print("[INFO] accessing video stream...")
video = cv2.VideoCapture(args["input"] if args["input"] else 1)

detector = SsdDetector()

while True:

  (grabbed, frame) = video.read()

  frame = detector.detect(frame, 0.5)

  cv2.imshow("Frame", frame)    
  key = cv2.waitKey(1) & 0xFF

  if key == ord("q"):
    break
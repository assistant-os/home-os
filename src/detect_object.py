import argparse
import requests
import cv2
import numpy as np
import os 

from utils.benchmark import Benchmark
from detectors.person_detector_ssd import PersonDetector as PersonDetectorSSD
from detectors.person_detector_yolo import PersonDetector as PersonDetectedYolo
from utils.recorder import Recorder

benchmark = Benchmark()

# construct the argument parser and parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("--video", type=str, default='', help="path to video")
ap.add_argument("--stream", type=str,default="", help="url to raspberry pi")
ap.add_argument("--algo", type=str, default="yolo", help="algo to use: yolo or ssd ")
ap.add_argument('-c', '--confidence', type=float, default=0.5,
							help='minimum probability to filter weak detections')
args = vars(ap.parse_args())

RADIUS = 10
RED = (0,0,255)

class Processor:
	def __init__(self):
		self.video = None
		self.recording = False	
		self.recordingRaw = False
		self.personDetector = None 
		if args["algo"] == "ssd":
			self.personDetector = PersonDetectorSSD()
		else:
			self.personDetector = PersonDetectedYolo()
		self.recorder = Recorder()


	def process(self, rawFrame):
		frame = rawFrame

		benchmark.pre()
		frame = self.personDetector.detect(rawFrame, 0.5)
		benchmark.post()

		(height, width) = frame.shape[:2]
		if self.recording or self.recordingRaw:
			cv2.circle(frame,(width - 2 * RADIUS, 2 * RADIUS), RADIUS, RED, -1)

		cv2.imshow('Video', frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			exit(0)
		elif key == ord("r"):
			if not self.recording:
				self.recorder.start(frame, os.path.join(os.path.dirname(__file__), '../datasets/video.process.avi'))
				self.recording = True
			else:
				self.recorder.stop()
				self.recording = False
		elif key%256 == 32:
			if not self.recordingRaw:
				self.recorder.start(frame, os.path.join(os.path.dirname(__file__), '../datasets/video.raw.avi'))
				self.recordingRaw = True
			else:
				self.recorder.stop()
				self.recordingRaw = False
		if self.recordingRaw:
				self.recorder.record(rawFrame)
		elif self.recording:
				self.recorder.record(frame)

processor = Processor()

if args["video"] != "":
	vidcap = cv2.VideoCapture(args["video"])

	fps = vidcap.get(cv2.CAP_PROP_FPS)
	success = True
	count = 0
	while success:
		success,frame = vidcap.read()

		if success:
			processor.process(frame)
else:
	r = requests.get(args["stream"], stream=True)
	if(r.status_code == 200):
		bytes = bytes()
		for chunk in r.iter_content(chunk_size=1024):
			bytes += chunk
			a = bytes.find(b'\xff\xd8')
			b = bytes.find(b'\xff\xd9')
			if a != -1 and b != -1:
				jpg = bytes[a:b+2]
				bytes = bytes[b+2:]
				rawFrame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
				processor.process(rawFrame)
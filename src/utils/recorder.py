import cv2
import os 

dirname = os.path.dirname(__file__)

class Recorder:

	def __init__(self):
		self.video = None

	def start(self, frame, filename):
			(height, width) = frame.shape[:2]

			if filename == "":
				filename = os.path.join(dirname, '../../datasets/video.avi')

			self.video = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (width, height))
			self.filename = filename

	def record(self, frame):
		self.video.write(frame)

	def stop(self):
		self.video.release()
		print("Video saved in ", self.filename)

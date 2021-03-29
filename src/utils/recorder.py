import cv2
import os 

dirname = os.path.dirname(__file__)

class Recorder:

	def __init__(self):
		self.video = None
		self.isRecording = False

	def start(self, frame, filename):
			(height, width) = frame.shape[:2]

			if filename == "":
				filename = os.path.join(dirname, '../../datasets/video.avi')

			self.video = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (width, height))
			self.filename = filename
			print("start record")

	def record(self, frame, filename = ""):
		if (self.video == None):
			self.start(frame, filename)

		self.video.write(frame)

	def stop(self):
		print("Video saved in ", self.filename)
		# self.video.release()

import cv2
import os
from benchmark import Benchmark
from person_detector import PersonDetector
import numpy as np 

dirname = os.path.dirname(__file__)

benchmark = Benchmark()
personDetector = PersonDetector()


vidcap = cv2.VideoCapture(os.path.join(dirname, '../benchmarks/datasets/video_recognize.avi'))
success = True
count = 0
for x in range(100):
	success,image = vidcap.read()
	count += 1
	image = np.array(np.rot90(image, k=2))

	benchmark.pre()
	personDetector.detect(image, 0.5)
	benchmark.post()


benchmark.stats()
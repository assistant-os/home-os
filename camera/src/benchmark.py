from imutils.video import FPS
import datetime
from statistics import mean, stdev 

class Benchmark:
	def __init__(self):
		self.fps = FPS().start() 
		self.computationDurations = []
		self.beforeComputation = None
		self.afterComputation = None
	
	def pre(self):
		self.beforeComputation = datetime.datetime.now()

	def post(self):
		self.fps.update()
		afterComputation = datetime.datetime.now()
		delta = afterComputation - self.beforeComputation
		print('delta', delta)
		deltaSeconds = delta.seconds + delta.microseconds /1E6
		self.computationDurations.append(deltaSeconds)

	def stats(self):
		self.fps.stop()

		print("[INFO] elapsed time: {:.2f}".format(self.fps.elapsed()))
		print("[INFO] approx. FPS: {:.2f}".format(self.fps.fps()))
		durations = self.computationDurations
		print("[INFO] computations: count: {}, mean: {:.3f}s, std: {:.3f}".format(len(durations), mean(durations), stdev(durations)))

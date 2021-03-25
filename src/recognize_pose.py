import cv2
import os
import imutils

# https://github.com/opencv/opencv/blob/master/samples/dnn/openpose.py

dirname = os.path.dirname(__file__)


protoFile = "pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
weightsFile = "pose/mpi/pose_iter_160000.caffemodel"

# Rea the network into Memory
net = cv2.dnn.readNetFromCaffe(
				os.path.join(dirname, '../models/pose/coco/pose_deploy_linevec.prototxt'),
				os.path.join(dirname, '../models/pose/coco/pose_iter_440000.caffemodel'))

imageName = os.path.join(dirname, '../datasets/yoga.png')

frame = cv2.imread(imageName)

frame = imutils.resize(frame, width=512)
(height, width) = frame.shape[:2]

blob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (width, height), (0, 0, 0), swapRB=False, crop=False)

# Set the prepared object as the input blob of the network
net.setInput(blob)

output = net.forward()
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
        cv2.circle(frame, (int(x), int(y)), 15, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
        cv2.putText(frame, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 3, lineType=cv2.LINE_AA)

        # Add the point to the list if the probability is greater than the threshold
        points.append((int(x), int(y)))
    else :
        points.append(None)

for pair in POSE_PAIRS:
    partA = pair[0]
    partB = pair[1]

    if points[partA] and points[partB]:
        cv2.line(frameCopy, points[partA], points[partB], (0, 255, 0), 3)

cv2.imshow("Output-Keypoints",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
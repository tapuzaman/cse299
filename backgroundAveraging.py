import numpy as np
import cv2

INST_WIDTH = 800
INST_HEIGHT = 600

class BackGroundSubtractor:

	def __init__(self,alpha,firstFrame):
		self.alpha  = alpha
		self.backGroundModel = firstFrame

	def getForeground(self,frame):

		self.backGroundModel =  frame * self.alpha + self.backGroundModel * (1 - self.alpha)



		return cv2.absdiff(self.backGroundModel.astype(np.uint8),frame)

cam = cv2.VideoCapture('../src/sample.avi')

# Just a simple function to perform
# some filtering before any further processing.
def denoise(frame):
    frame = cv2.medianBlur(frame,5)
    frame = cv2.GaussianBlur(frame,(5,5),0)

    return frame

ret,frame = cam.read()
frame = cv2.resize(frame, (INST_WIDTH, INST_HEIGHT))
if ret is True:
	backSubtractor = BackGroundSubtractor(0.01,denoise(frame))
	run = True
else:
	run = False

while(run):
	# Read a frame from the camera
	ret,frame = cam.read()
	frame = cv2.resize(frame, (INST_WIDTH, INST_HEIGHT))

	# If the frame was properly read.
	if ret is True:
		# Show the filtered image
		cv2.imshow('input',denoise(frame))

		# get the foreground
		foreGround = backSubtractor.getForeground(denoise(frame))

		# Apply thresholding on the background and display the resulting mask
		ret, mask = cv2.threshold(foreGround, 15, 255, cv2.THRESH_BINARY)

		# display a grayscale image by converting 'foreGround' to
		# a grayscale before applying the threshold.
		cv2.imshow('mask',mask)

		key = cv2.waitKey(10) & 0xFF
	else:
		break

	if key == 27:
		break

cam.release()
cv2.destroyAllWindows()

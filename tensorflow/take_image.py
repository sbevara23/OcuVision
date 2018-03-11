import pyavfcam
from PIL import Image


# Open the default video source
cam = pyavfcam.AVFCam(sinks='image')
cam.snap_picture('tensorflow/image.jpg')
img = Image.open('tensorflow/image.jpg')
img.show()
#print "Saved test.jpg (Size: " + str(cam.shape[0]) + " x " + str(cam.shape[1]) + ")"

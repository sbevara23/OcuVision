import pyavfcam

# Open the default video source
cam = pyavfcam.AVFCam(sinks='image')
cam.snap_picture('image.jpg')

print "Saved test.jpg (Size: " + str(cam.shape[0]) + " x " + str(cam.shape[1]) + ")"

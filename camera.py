import picamera
camera = picamera.PiCamera()
camera.resolution = (800, 600)
camera.start_preview()
sleep(5)
camera.capture(‘snapshot.jpg’, resize=(640, 480))
camera.stop_preview()
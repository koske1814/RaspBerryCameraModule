import picamera
import time
import sg90
import sys

def take_photo():
    s = sg90.sg90(12,0)
    with picamera.PiCamera() as camera:
        camera.resolution = (512,389)
        camera.start_preview()
        time.sleep(2)
        s.setdirection(45,10)    
        camera.capture('static/img/image1.jpg')
        s.setdirection(0,10)    
        time.sleep(2)
        camera.capture('static/img/image2.jpg')
        s.setdirection(-45,-10)    
        time.sleep(2)
        camera.capture('static/img/image3.jpg')
        s.cleanup()

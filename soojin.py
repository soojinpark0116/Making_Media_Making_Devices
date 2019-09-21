from picamera import PiCamera
from gpiozero import Button
from time import sleep

camera = PiCamera()
whiteButton = Button(14) #used 14 just as an example

#flip camera
camera.hflip = True 
camera.vflip = True
#set resolution
camera.resolution = (1280, 720)
#set brightness
camera.brightness = 70

#take 10 shots
for i in range(10):
	whiteButton.wait_for_press()
	camera.capture('shot{0:04d}.jpg'.format(i)) #4 digits for file name
	sleep(3) #set interval

#convert to GIF
system('convert -delay 10 -loop 0 shot*.jpg movingimage.gif')
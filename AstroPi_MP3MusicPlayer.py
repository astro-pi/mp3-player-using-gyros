import time       #Begin by importing in all the things we need
import os
import subprocess
from sense_hat import SenseHat
from pygame.locals import *
import pygame
import RPi.GPIO as GPIO


def send_key_press(key):    #This function reads which key is within the brackets and does what that key woudl do. For eaxmple if it were a '-' symbol it would decrease the sound because that is what the '-' symbol does when pressed on a keyboard when using omxplayer
    global proc
    proc.stdin.write(key.encode('utf-8'))
    proc.stdin.flush()

""" As shown in the next 5 functions the code:
    
     sense.set_pixels(    )
     time.sleep(1)
     sense.set_pixels(music)

    What this code will do is set the LED Matrix to a image specific to that function (eg: a pause symbol for the Pause() function) and then wait for 1 second before moving back to the homescreen (music)

     Something else that happens in the following functions is the function send_key_press() which has been defined above.
     This means, for eaxample, that if the Plus() function is activated then it would look at send_key_press() and what key is within the brackets.
     In this case the key is '+' which, if had it been pressed on a keyboard would increase the volume.
     Therefore if the Plus() function is called it would also increase the volume similar to that of a key press


    """

def Back():       #This function skips back 30 seconds of the track
    send_key_press('/x1B[D') #left arrow key
    sense.set_pixels(rewind)
    time.sleep(1)
    sense.set_pixels(music)

def Forwards():       #This function skips forward 30 seconds of the track 
    send_key_press('/x1B[C') #right arrow key
    sense.set_pixels(fast_forward)
    time.sleep(1)
    sense.set_pixels(music)

def Plus():      #This function increases the volume by 3 decibels
    send_key_press('+')
    sense.set_pixels(plus)
    time.sleep(1)
    sense.set_pixels(music)

def Less():     #This function decreases the volume by 3 decibels
    send_key_press('-')
    sense.set_pixels(less)
    time.sleep(1)
    sense.set_pixels(music)

def Pause():       #This function pauses the track when pressed once, if pressed against it plays the track
    send_key_press('p')
    sense.set_pixels(pause)
    time.sleep(1)
    sense.set_pixels(music)

#Before looking at the next 2 functions is it worth noting that the variable 'x' will later be shown to be the song number in the array 'playArray'
    

def Next(stopOrNot):      #This function skips to the next track
    global x
    global nextTrack
    global number_of_mp3_files_in_directory
    #first stop current track
    if stopOrNot == 1:
            send_key_press('q')
    x += 1 #When skipping to the next track 'x' (the song number) has 1 added to it, setting it to the next value in playArray (a.k.a the next song)
    if x >= number_of_mp3_files_in_directory: #This checks to see whether X is bigger than the number_of_mp3_files_in_directory
        x = 0      #If it is the variable 'X' is set back to 0  (the first song)
    nextTrack = True   #nextTrack is set to True
    time.sleep(1)

def Prev():      #This function skips back to the previous track
    global x
    global nextTrack
    global number_of_mp3_files_in_directory
    #first stop current track
    send_key_press('q')
    if x == 0: #If x is equal to 0: (the first song)
        x = number_of_mp3_files_in_directory - 1  # x is then set to the number_of_mp3_files_in_directory minus 1, meaning that x has looped from the first track back to the 2nd last track
    else:
        x -= 1  #If x is not equal to 0 (it is not the last track) then subtract 1 from x. This means that x is now equal to the previous value (the previous song)
    nextTrack = True
    time.sleep(1)


w = [150, 150, 150] #This sets the variable 'w' to the colour white
r = [255, 0, 0] #This sets the variable 'r' to the colour red

#Below are different images created by setting each pixel of the 64 bit LED Matrix to a variable. This means that a pixel with the variable 'r' will be shown as red.
#By creating these image they are able to be called by using the code 'sense.set_pixels(music)' setting the LED Matric to the music image 

music = [
w,w,w,w,w,w,w,w, #As an example line line would be completely white
w,w,r,r,r,r,r,w,
w,w,r,w,w,w,r,w,
w,w,r,w,w,w,r,w,
w,w,r,w,w,w,r,w,
r,r,r,w,r,r,r,w,
r,r,r,w,r,r,r,w,
w,w,w,w,w,w,w,w
]

pause = [
w,w,w,w,w,w,w,w,
w,r,r,w,w,r,r,w,
w,r,r,w,w,r,r,w,
w,r,r,w,w,r,r,w,
w,r,r,w,w,r,r,w,
w,r,r,w,w,r,r,w,
w,r,r,w,w,r,r,w,
w,w,w,w,w,w,w,w
]

forward = [
w,w,w,w,r,w,w,w,
w,w,w,w,r,r,w,w,
w,w,w,w,r,r,r,w,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
w,w,w,w,r,r,r,w,
w,w,w,w,r,r,w,w,
w,w,w,w,r,w,w,w
]

back = [
w,w,w,r,w,w,w,w,
w,w,r,r,w,w,w,w,
w,r,r,r,w,w,w,w,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
w,r,r,r,w,w,w,w,
w,w,r,r,w,w,w,w,
w,w,w,r,w,w,w,w
]

plus = [
w,w,w,w,w,w,w,w,
w,w,w,r,r,w,w,w,
w,w,w,r,r,w,w,w,
w,r,r,r,r,r,r,w,
w,r,r,r,r,r,r,w,
w,w,w,r,r,w,w,w,
w,w,w,r,r,w,w,w,
w,w,w,w,w,w,w,w
]

less = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,r,r,r,r,r,r,w,
w,r,r,r,r,r,r,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

fast_forward = [
w,w,w,w,w,w,w,w,
r,r,w,w,r,r,w,w,
r,w,r,w,r,w,r,w,
r,w,w,r,r,w,w,r,
r,w,w,r,r,w,w,r,
r,w,r,w,r,w,r,w,
r,r,w,w,r,r,w,w,
w,w,w,w,w,w,w,w
]

rewind = [
w,w,w,w,w,w,w,w,
w,w,r,r,w,w,r,r,
w,r,w,r,w,r,w,r,
r,w,w,r,r,w,w,r,
r,w,w,r,r,w,w,r,
w,r,w,r,w,r,w,r,
w,w,r,r,w,w,r,r,
w,w,w,w,w,w,w,w
]

pygame.init()
pygame.display.set_mode((40,40))  #This sets the display mode to 40,40

#Set GPIO pins
UP = 26  #This code sets the variable 'UP' to the number 26. This will be used below.
DOWN = 13
LEFT = 20
RIGHT = 19
A = 16
B = 21

GPIO.setmode(GPIO.BCM)

for pin in [UP, DOWN, LEFT, RIGHT, A, B]: 
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

sense = SenseHat()

sense.set_pixels(music)   #This sets the LED Matrix to the 'music' image until otherise specified

#threshold sets the sensitivity of the gyroscope movements
threshold = 4.0

#This is the folder that the music is stored in
playlistFolder = 'home/pi/Music'
strFind = 'find /' + playlistFolder + '/*.mp3 > playlist.txt'
print(strFind)    #This will print 'find /home.pi/Music/*.mp3 > playlist.txt'
os.system(strFind)

plist = open('playlist.txt')   #The variable 'plist' is set to the open folder of playlist.txt
playArray = plist.read().splitlines()    #The variable playArray is set to plist text split into seperate lines
number_of_mp3_files_in_directory = len(playArray)    #The variable 'number_of_mp3_files_in_directory' is set to the length of playArray (how many lines there is in playArray)
print(number_of_mp3_files_in_directory)    #This should print how many lines there are in playArray, which is also the amount of mp3 files in the home/pi/Music folder
x = 0
nextTrack = True

file = playArray[x]    #This sets the variable file to the name of the first mp3 file in playArray (the first song name)
print(file)   #This will print file (it will print the first song's name or what it has been labelled as)
proc = subprocess.Popen(["omxplayer", file, "-o", "local", "-I"],
stdin = subprocess.PIPE,
stdout = subprocess.PIPE,
stderr = subprocess.PIPE,
close_fds=True)
nextTrack = False

while True: #This is a while loop that will continue forever until the code stops running
	if nextTrack == True:  #If the the code has been told to skip to the next track the following code will run
		file = playArray[x]  #Because x is no longer set as 0 (when the track changes 1 is added to x) file is set to the 2nd value is PlayArray (the second mp3 file)
		print(file) #It will print the next song
		proc = subprocess.Popen(["omxplayer", file, "-o", "local", "-I"],
		stdin = subprocess.PIPE,
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE,
		close_fds=True)
		nextTrack = False
	
	#need to automatically move to next track
	if proc.poll() is not None:
		Next(0)
	for event in pygame.event.get():
		if event.type == KEYDOWN: #If the joystick is pressed a direction:
			if event.key == K_LEFT: #If the joystick is pressed to the left the Prev() function will run (it will skip back to the previous track)
				Prev()
			if event.key == K_RIGHT: #If the joystick is pressed to the right the Next(1) function will run (it will skip to the next track)
				Next(1)
			if event.key == K_UP: #If the joystick is pressed up the Plus() function will run (the volume will increase)
				Plus()
			if event.key == K_DOWN: #If the joystick is pressed downwards the Less() function will run (the volume will decrease)
				Less()
			if event.key == K_RETURN: #If the joystick is pressedin the center the Pause() function will run (the music will pause)
				Pause()


	if GPIO.input(LEFT) == False:
		Back() #If the left button (from the 4 button diamond shape arangement) is pressed the Back() function will run
	if GPIO.input(RIGHT) == False:
		Forwards() #If the right button is pressed then the Forwards() function will run
	if GPIO.input(UP) == False:
		Plus() #If the up button (the one at the top) is pressed then the Plus() function will run
	if GPIO.input(DOWN) == False:
		Less() #If the down button (the one at the bottom) is pressed then the Less() function will run
	if GPIO.input(A) == False:
		Prev() #If button A (the left button of the pair of buttons beneath the first 4) is pressed then the Prev() function will run
	if GPIO.input(B) == False:
		Next(1) #If button B (to the right of button A) is pressed then the Next(1) function will run

	#shake routines to call prev and next
	pitch, roll, yaw = sense.get_gyroscope_raw().values()
	if yaw > threshold:
		pitch = round(pitch, 1) #This sets the variable 'pitch' to the gyroscope measurement of pitch rounded to one place
		roll = round(roll, 1) #This sets the variable 'roll' to the gyroscope measurement of roll rounded to one place
		yaw = round(yaw, 1) #This sets the variable 'yaw' to the gyroscope measurement of yaw rounded to one place      
		print ("%s %s %s" % (pitch, roll, yaw)) 
		sense.set_pixels(less)
		Less() #If the MP3 Music Player is tilted right from a 90 degrees position with the screen facing the user the Less() function will run 
	if yaw < -threshold:	
		pitch = round(pitch, 1)
		roll = round(roll, 1)
		yaw = round(yaw, 1)      
		print ("%s %s %s" % (pitch, roll, yaw)) 
		sense.set_pixels(plus)
		Plus() #If the MP3 Music Player is tilted left from a 90 degrees position with the screen facing the user the Plus() function will run
	#Could be used to replicate other functionality
	#if pitch > threshold: 
	#	pitch = round(pitch, 1)
	#	roll = round(roll, 1)
	#	yaw = round(yaw, 1)      
	#	print ("%s %s %s" % (pitch, roll, yaw)) 
	#	sense.show_letter("U")
	#if pitch < -threshold:	
	#	pitch = round(pitch, 1)
	#	roll = round(roll, 1)
	#	yaw = round(yaw, 1)     
	#	print ("%s %s %s" % (pitch, roll, yaw)) 
	#	sense.show_letter("D")			
	if roll > threshold: 
		pitch = round(pitch, 1)
		roll = round(roll, 1)
		yaw = round(yaw, 1)      
		print ("%s %s %s" % (pitch, roll, yaw)) 
		sense.set_pixels(back)
		Prev() #If the MP3 Music Player is tilted forwards from a 90 degrees position with the screen facing the user the Prev() function will run
	if roll < -threshold:	
		pitch = round(pitch, 1)
		roll = round(roll, 1)
		yaw = round(yaw, 1)     
		print ("%s %s %s" % (pitch, roll, yaw)) 
		sense.set_pixels(forward)
		Next(1)	#If the MP3 Music player is tilted backwardsfrom a 90 degress position with the screen facing the user then Next(1) function will run		
	

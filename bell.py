import RPi.GPIO as GPIO
import time
import os
import glob
#GPIO SETUP
GPIO.setmode(GPIO.BCM)
Button = 21
n = 1
GPIO.setup(Button,GPIO.IN)
#loop
print("Program Running")
while 1 == 1:#loops forever till keyboard interupt (ctr + C) 
  if GPIO.input(Button) == False:#when button pressed:
    print("Button Pressed")
    
    #    ------|    photo & Bell    |------ #
    #Get FileName
    now = time.strftime("Date%m-%d-%yTime%H-%M-%S")
    #Make command to run OCMMDS
    command = "bash oscmds.sh " +  str(now)
    
    # -- OSMC.sh is an Shell script that
    # -- is responsible for taking the picture and
    # -- Making the Doorbell Noise
    
    # --- We insert the "Now" argument so the python
    # --- script knows what the file name of the
    # --- picture will be so it can pass it on into the
    # --- email script (so it knows what file to email
    
    #run command
    os.system(command)
    #diagnostics
    print("Filename:", now)
    
  
    # ----| Email     |---- #
    print("Email")#email
    emailcommand = 'python3 IOTNOTIFY2.py "Someone is at the door"' + ' "photos/' + now + '.jpg"'
    os.system(emailcommand) #running the Email script with:
    #-- the subject as "Someone is at the door" and the filename
    #-- We made before at the -Photo & Bell- section
    
    # -- End Diagnostic Info
    print("Done Process")
    #-space out for next "Press of Button"
    print("")
    print("")


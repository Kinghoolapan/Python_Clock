#we are going to build a clock in python
#first letd make it so we can set the second minute and hour

seconds = 56
minutes = 59
hours = 23

#next, lets import time for the time.sleep(x) function
import time

#now, we build a loop for seconds
while True:
    print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours + 1
    if hours == 24:
        hours = 0
        minutes = 0
        seconds = 0
       
    
    #so far, this will increase the seconds and then have python wait for 1 second
    

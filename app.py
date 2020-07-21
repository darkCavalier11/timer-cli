# timer
import time
import math
import sys
from playsound import playsound


try:
    time_in_second = math.floor(float(sys.argv[1])*60)
    
    while time_in_second and time_in_second > 0:
        print(str(time_in_second) + ' seconds left ', end='\r')
        time.sleep(1)
        time_in_second -= 1
    print('\n\n')
except IndexError:
    print('Invalid Input')

playsound('got-it-done.ogg')
print('TIME OVER')

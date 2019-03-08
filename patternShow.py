import os
import time
import numpy as np
import cv2 as cv
from PIL import Image
# Import luma stuff

def showPatterns():
    directory = 'patterns'
    cap = cv.VideoCapture(0)
    fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
    for filename in os.listdir(directory):
        # print(os.path.join(directory, filename))
        with open(os.path.join(directory, filename)) as f:
            lines = f.readlines()
            for line in lines:
                leds = line.split(",")
                #TODO show leds for each line
                #with canvas(device) as draw:
                    #TODO loop over columsn and rows displaying or turning off leds
                    #draw.point((x,y), fill white)

                ret, frame = cap.read()
                fgmask = fgbg.apply(frame)
                cv.imshow('frame',fgmask)
                #TODO take picture if white balance hits over certain amount.


#cap = cv2.VideoCapture(0)
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(500, 16, 0, 80)
#while(1):
#    ret, frame = cap.read()
#    fgmsk = fgbg.apply(frame)
#    bgSum = cv2.sumElems(fgmsk)
#    if bgSum[0] > 10000:
#       print("Face")
#    else:
        #print("No Face")
#    cv2.imshow('frame',fgmsk)
# 
#cap.release()
#cv2.destroyAllWindows()

if __name__ == "__main__":
    showPatterns()
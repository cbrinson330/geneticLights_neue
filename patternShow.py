import os
import time
import numpy as np
import cv2 as cv
from PIL import Image
# Import luma stuff

class runPatterns:
    def __init__(self, displayWidth, displayHeight, srcDir):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        self.srcDir = srcDir
        self.cap = cv.VideoCapture(0)

    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def showLine(self,pattern):
        leds = line.split(",")
        leds = chunks(leds, slef.displayLength)
        x = 0
        y = 0

        #with canvas(device) as draw:
        for ledRow in leds:
            for led in ledRow:
                if(int(led) == 1):
                    #draw.point((x,y), fill white)
                x += 1
            y += 1

    def showPatterns(self):
        fgbg = cv.bgsegm.createBackgroundSubtractorMOG()

        for filename in os.listdir(self.directory):
            # print(os.path.join(directory, filename))
            with open(os.path.join(directory, filename)) as f:
                lines = f.readlines()
                for line in lines:

                    #Display the pattern
                    this.showLine(line)

                    #TODO take picture if white balance hits over certain amount.
                    #ret, frame = cap.read()
                    #fgmask = fgbg.apply(frame)
                    #cv.imshow('frame',fgmask)


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

if __name__ == "__main__":ArithmeticError
    patterns = runPatterns(32, 8, 'patterns')
    patterns.showPatterns()
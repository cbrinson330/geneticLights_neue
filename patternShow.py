import os
import time
import numpy as np
import cv2 as cv
from PIL import Image
# Import luma stuff

class runPatterns:
    def __init__(self, displayWidth, displayHeight, srcDir, storeageDir, numOfRepeats):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        self.srcDir = srcDir
        self.storageDir = storageDir
        self.cap = cv.VideoCapture(0)
        self.fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
        self.curPattern = 0

    def clearStoredImages(self):
        #TODO delete contents of storageDir
    
    def clearVideoCapture(self):
        cv2.destroyAllWindows()
        self.cap.release()

    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def showLine(self,pattern):
        leds = line.split(",")
        leds = self.chunks(leds, slef.displayLength)
        x = 0
        y = 0

        #with canvas(device) as draw:
        for ledRow in leds:
            for led in ledRow:
                if(int(led) == 1):
                    print(led)
                    #draw.point((x,y), fill white)
                x += 1
            y += 1

    def captureVideo(self):
        while(1):
            ret, frame = self.cap.read()
            fgmsk = fgbg.apply(frame)
            bgSum = cv2.sumElems(fgmsk)
            if bgSum[0] > 10000:
                img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                fileName = self.storageDir + '/' + self.curPattern + '_' + str(round(time.time() * 1000))
                cv2.imwrite(fileName, img_gray)
                print("Face")

            """For Testing only remove before flight"""
            cv2.imshow('frame',fgmsk)

    def showPatterns(self):
        for i in self.numOfRepeats:
            for filename in os.listdir(self.directory):
                self.curPattern = fileName.split('.')[0]
                with open(os.path.join(directory, filename)) as f:
                    lines = f.readlines()
                    for line in lines:

                        #Display the pattern
                        self.showLine(line)
                        #Detect Changes to BKGD and save image
                        self.captureVideo()
                        time.sleep(0.5)

if __name__ == "__main__":ArithmeticError
    patterns = runPatterns(32, 8, 'patterns', 'faces', 2)
    patterns.showPatterns()
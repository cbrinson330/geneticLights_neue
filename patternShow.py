import os
import time
import thread
import datetime
import numpy as np
import cv2 as cv
from PIL import Image
# Import luma stuff

class runPatterns:
    def __init__(self, displayWidth, displayHeight, srcDir, storageDir, numOfRepeats, stepLength):
        self.displayHeight = displayHeight
        self.displayWidth = displayWidth
        self.srcDir = srcDir
        self.storageDir = storageDir
        self.cap = cv.VideoCapture(0)
        self.fgbg = cv.bgsegm.createBackgroundSubtractorMOG(5000, 16, 0.80)
        self.curPattern = 0
        self.numOfRepeats = numOfRepeats
        self.stepLength = stepLength

    def _clearVideoCapture(self):
        cv2.destroyAllWindows()
        self.cap.release()

    def _chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def _showLine(self,pattern):
        leds = pattern.split(",")
        leds = self._chunks(leds, self.displayWidth)
        x = 0
        y = 0

        #with canvas(device) as draw:
        for ledRow in leds:
            for led in ledRow:
                if(int(led) == 1):
                    foo = int(led)
                    #draw.point((x,y), fill white)
                x += 1
            y += 1

    def _captureVideo(self):
        while(1):
            ret, frame = self.cap.read()
            fgmsk = self.fgbg.apply(frame)
            bgSum = cv.sumElems(fgmsk)
            if bgSum[0] > 10000:
                img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                curTime = datetime.datetime.now()
                timestamp = "%s%s%s" % (curTime.minute, curTime.second, str(curTime.microsecond))
                fileName = self.storageDir + '/' + self.curPattern + '_' + timestamp + '.jpg'
                cv.imwrite(fileName, img_gray)
                #TODO consider puttin delay in to limit the frame rate

    def showPatterns(self):
        thread.start_new_thread(self._captureVideo,())
        for i in range (1, int(self.numOfRepeats)):
            for filename in os.listdir(self.srcDir):
                self.curPattern = filename.split('.')[0]
                with open(os.path.join(self.srcDir, filename)) as f:
                    lines = f.readlines()
                    for line in lines:

                        #Display the pattern
                        self._showLine(line)
                        time.sleep(self.stepLength)
            i += 1

if __name__ == "__main__":
    patterns = runPatterns(32, 8, 'patterns', 'faces', 2, 0.5)
    patterns.showPatterns()
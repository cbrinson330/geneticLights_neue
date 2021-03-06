import os
import time
import _thread
import datetime
import numpy as np
import cv2 as cv
from PIL import Image
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from luma.core.render import canvas

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
        self.serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(self.serial, cascaded=4, block_orientation=90, rotate=0)

    def _clearVideoCapture(self):
        cv.destroyAllWindows()
        self.cap.release()

    def _chunks(self, l, n):
        #Yield successive n-sized chunks from l.
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def _showLine(self,pattern):
        leds = pattern.split(",")
        leds = list(self._chunks(leds, self.displayWidth))
        y = 0

        with canvas(self.device) as draw:
            for ledRow in leds:
                x = 0
                for led in ledRow:
                    if(int(led) == 1):
                        draw.point((x,y), fill="white")
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
                time.sleep(self.stepLength/4)

    def showPatterns(self):
        _thread.start_new_thread(self._captureVideo,())
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
        self._clearVideoCapture()

if __name__ == "__main__":
    patterns = runPatterns(32, 8, 'patterns', 'faces', 2, 0.5)
    patterns.showPatterns()

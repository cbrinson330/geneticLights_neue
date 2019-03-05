import os
import numpy as np
import cv2 as cv

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

                ret, frame = cap.read()
                fgmask = fgbg.apply(frame)
                cv.imshow('frame',fgmask)
                #TODO take picture if white balance hits over certain amount.

if __name__ == "__main__":
    showPatterns()
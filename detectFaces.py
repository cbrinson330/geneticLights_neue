import os
import numpy as np
import urllib
import operator
import cv2 as cv
from PIL import Image

class detectFaces:

    def __init__ (self, imgDir, numberOfPatterns, patternOrderFile, patternsDir):
        self.imgDir = imgDir 
        self.store = {}
        self.patternsDir = patternsDir
        self.numberOfPatterns = numberOfPatterns
        self.patternOrderFile = patternOrderFile

        self._initStore()


    def _urlToImage(self, url):
	    resp = urllib.urlopen(url)
	    image = np.asarray(bytearray(resp.read()), dtype="uint8")
	    image = cv.imdecode(image, cv.IMREAD_GRAYSCALE)
	    return image

    def _initStore(self):
        path, dirs, files = next(os.walk(self.patternsDir))
        patternCount = len(files)
        i = 0
        while i < patternCount:
            self.store[str(i)] = 0
            i+=1

    def _outputPatternOrder(self):
        sortedPatterns = sorted(self.store.items(), key=operator.itemgetter(1))
        sortedPatterns = reversed(sortedPatterns)

        fileName = self.patternOrderFile
        f = open(fileName, "w")

        for key,value in sortedPatterns:
            line = str(key) + '\n'
            f.write(line)
        
        f.close()
    
    def detectFaceForImage(self):
        for fileName in os.listdir( self.imgDir ):
            fileNamePt = fileName.split('_')
            patternId = fileNamePt[0]
            faceCascade = cv.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
            
            imgUrl = self.imgDir + '/' + fileName
            img = self._urlToImage(imgUrl)

            faces = faceCascade.detectMultiScale(
                img,
                scaleFactor=1.1,
                minNeighbors=5, 
                minSize=(30, 30)
            )

            self.store[str(patternId)] += len(faces)

            #Delete file
            os.remove(imgUrl)
        
        self._outputPatternOrder()

if __name__ == "__main__":
    df = detectFaces()
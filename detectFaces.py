import os
import numpy as np
import urllib
import cv2 as cv
from PIL import Image

class detectFaces:

    def __init__ (self):
        self.imgDir = "faces"
        self.store = {}
        self.initStore()
        self.numberOfPatterns = 60


    def url_to_image(self, url):
	    resp = urllib.urlopen(url)
	    image = np.asarray(bytearray(resp.read()), dtype="uint8")
	    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
	    return image

    def initStore(self):
        patternCount = len([name for name in os.listdir('patterns') if os.path.isfile(name)])
        i = 0
        while i < patternCount:
            self.store[i] = 0
            i+=1
    
    def getCounts(self):
        return self.store

    def detectFaceForImage(self):
        for filename in oslistdir(self.imgDir)
            fileNamePt = fileName.split('.')
            patternId = fileNamePt.split('_')[0]
            
            imgUrl = self.imgDir + '/' + filename
            img = self.url_to_image(imgUrl)

            faces = faceCascade.detectMultiScale(
                img,
                scaleFactor=1.1,
                minNeighbors=5, 
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            len(faces)
            self.store[patternId] += len(faces)

            #Delete file
            os.remove(imgUrl)
        

if __name__ == "__main__":
    df = detectFaces()
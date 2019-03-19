from patternShow import runPatterns
from detectFaces import detectFaces
#import population

if __name__ == "__main__":
    #Dir paths
    patternStorageDir = 'patterns'
    imgStorageDir = 'faces'

    #Display vars
    displayWidth = 32
    displayHeight = 9
    timesToRepeatAllPatterns = 2
    stepLength = 0.5 #Num of secs between each line in a pattern

    #Patterns
    numberOfPatterns = 60

    while True:
        rp = runPatterns(displayWidth, displayHeight, patternStorageDir, imgStorageDir, timesToRepeatAllPatterns, stepLength)
        rp.showPatterns()

        #TODO calculate faces seen
        df = detectFaces(imgStorageDir, numberOfPatterns)
        df.detectFaceForImage()

        #TODO order patterns based on number of faces seen
        #TODO pop = Population(size=60, crossover=0.8, elitism=0.1, mutation=0.3)
        #TODO pop.evolve()
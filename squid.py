from patternShow import runPatterns
from detectFaces import detectFaces
#import population

if __name__ == "__main__":
    #Dir paths
    patternStorageDir = 'patterns'
    imgStorageDir = 'faces'
    patternOrderFile = 'patternRanking.txt'

    #Display vars
    displayWidth = 32
    displayHeight = 9
    timesToRepeatAllPatterns = 2
    stepLength = 0.5 #Num of secs between each line in a pattern

    #Patterns
    numberOfPatterns = 60

    #while True:
    print("starting show patterns")
    #rp = runPatterns(displayWidth, displayHeight, patternStorageDir, imgStorageDir, timesToRepeatAllPatterns, stepLength)
    #rp.showPatterns()
    print("done showing Patterns")

    print("starting detect faces")
    df = detectFaces(imgStorageDir, numberOfPatterns, patternOrderFile, patternStorageDir)
    df.detectFaceForImage()
    print("done detecting faces")

    #TODO pop = Population(size=60, crossover=0.8, elitism=0.1, mutation=0.3)
    #TODO pop.evolve()
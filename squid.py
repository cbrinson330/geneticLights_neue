from patternShow import runPatterns
from detectFaces import detectFaces
from evolve import Population

if __name__ == "__main__":
    #Paths
    patternStorageDir = 'patterns'
    imgStorageDir = 'faces'
    patternOrderFile = 'patternRanking.txt'

    #Display
    displayWidth = 32
    displayHeight = 9
    timesToRepeatAllPatterns = 2
    stepLength = 0.5 #Num of secs between each line in a pattern

    #Patterns
    numberOfPatterns = 60
    stepTime = 0.5 #Length (secs) to play for pattern
    playTime = 10 #Length (secs) pattern should last
    numberOfLeds = displayHeight * displayWidth
    numberOfSteps = playTime / stepTime


    #while True:
    print("Starting show patterns")
    #rp = runPatterns(displayWidth, displayHeight, patternStorageDir, imgStorageDir, timesToRepeatAllPatterns, stepLength)
    #rp.showPatterns()
    print("Finished showing Patterns")

    print("Starting detect faces")
    #df = detectFaces(imgStorageDir, numberOfPatterns, patternOrderFile, patternStorageDir)
    #df.detectFaceForImage()
    print("Finished detecting faces")

    print("Starting Evolve")
    pop = Population(patternOrderFile, 60, 0.8, 0.1, 0.3, patternStorageDir)
    pop.evolve()
    print("Finished Evolving")
from patternShow import runPatterns
#import population
#import detecFaces

if __name__ == "__main__":
    #Dir paths
    patternStorageDir = 'patterns'
    imgStorageDir = 'faces'

    #Display vars
    displayWidth = 32
    displayHeight = 9
    timesToRepeatAllPatterns = 2
    #Num of secs between each line in a pattern
    stepLength = 0.5




    while True:
        rp = runPatterns(displayWidth, displayHeight, patternStorageDir, imgStorageDir, timesToRepeatAllPatterns, stepLength)
        rp.showPatterns()

        #TODO show patterns
        #TODO pop = Population(size=60, crossover=0.8, elitism=0.1, mutation=0.3)
        #TODO pop.evolve()
        #TODO calculate faces seen
        #TODO order patterns based on number of faces seen
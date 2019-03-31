import os
import random

class patternGen():
    @staticmethod
    def genPatterns(numOfPatterns, playTime, stepTime, numOfLeds, patternDir):
        numOfSteps = playTime / stepTime

        i = 0
        while i < numOfPatterns:
            fileName = patternDir + '/' + str(i) + '.txt'
            f = open(fileName, "w")

            j = 0
            while j < numOfSteps:
                line = ''

                k = 0
                while k < numOfLeds:
                    int = random.randint(0,1)
                    if k == 0:
                        line += str(int)
                    else:
                        line += ',' + str(int)

                    if k == numOfLeds - 1:
                        line += '\n'
                    k+=1
                f.write(line)
                j+=1
            f.close()
            i+=1
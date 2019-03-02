import os

def showPatterns():
    directory = 'patterns'
    for filename in os.listdir(directory):
        print(os.path.join(directory, filename))
        with open(os.path.join(directory, filename)) as f:
            lines = f.readlines()
            print(lines)
            #TODO show leds for each line
            #TODO run background check at the same time
            #TODO take picture if white balance hits over certain amount.

if __name__ == "__main__":
    showPatterns()
from random import (choice, random, randint)
import os

__all__ = ['Chromosome', 'Population']

class Chromosome:
    def __init__(self, gene, fitness=0, id=0):
        self.gene = gene
        self.fitness = fitness
        self.id = id
    
    def mate(self, mate):
        pivot = randint(0, len(self.gene) - 1)
        gene1 = self.gene[:pivot] + mate.gene[pivot:]
        gene2 = mate.gene[:pivot] + self.gene[pivot:]
        
        return Chromosome(gene2), Chromosome(gene2)
    
    def mutate(self):
        totalLEDS = 0
        gene = list(self.gene)

        for i in list(gene):
            totalLEDS += len(list(i))
        
        percent = totalLEDS/100
        tenPercent = int(percent*10)

        for i in range(tenPercent):
            step = randint(0, len(gene) - 1)
            led = randint(0, len(list(gene[0])) - 1)
            if(gene[step][led] == 0): gene[step][led] = 1
            else:
                gene[step][led] = 0

        return Chromosome(gene)

    @staticmethod            
    def _update_fitness(gene):
        fitness = 0
        for a, b in zip(gene, Chromosome._target_gene):
            fitness += abs(ord(a) - ord(b))
            
        return fitness
        
class Population:
    _tournamentSize = 3

    def __init__(self, 
                 patternOrderFile,
                 size=1024,
                 crossover=0.8,
                 elitism=0.1,
                 mutation=0.03,
                 patternDir='patterns'):

        self.elitism = elitism
        self.mutation = mutation
        self.crossover = crossover
        self.patternDir = patternDir
        self.patternOrderFile = patternOrderFile
        self.population = list(sorted(self._getPatterns(), key=lambda x: x.fitness))

    def _getPatterns(self):
        patternDict = {}
        buffer = []
        i = 0

        #Get dict of patterns with rankings
        with open(self.patternOrderFile) as f:
            lines = f.readlines()
            for line in lines:
                patternDict[str(line).rstrip()] = i
                i += 1
                

        for fileName in os.listdir(self.patternDir):
            patternId = fileName.split('.')[0]
            fitness = patternDict[patternId]
            geneBuf = []
            with open(os.path.join(self.patternDir, fileName)) as f:
                lines = f.readlines()
                for line in lines:
                    cleanLine = line.rstrip()
                    geneBuf.append(cleanLine.split(','))
            buffer.append(Chromosome(geneBuf, fitness, patternId))

        return buffer

    def _outputPatterns(self):
        i = 0
        for chrome in self.population:
            fileName = self.patternDir + '/' + str(i) + '.txt'
            f = open(fileName, "w")
            for step in chrome.gene:
                line = ''
                ledNum = 0
                for led in step:
                    line += str(led)
                    if ledNum == len(step) - 1:
                        line += '\n'
                    else:
                        line += ','
                    ledNum += 1
                f.write(line)
            f.close()
            i += 1

    def _tournament_selection(self):
        best = choice(self.population)
        for i in range(Population._tournamentSize):
            cont = choice(self.population)
            if (cont.fitness < best.fitness): best = cont
                    
        return best

    def _selectParents(self):
        return (self._tournament_selection(), self._tournament_selection())
        
    def evolve(self):
        size = len(self.population)
        idx = int(round(size * self.elitism))
        buf = self.population[:idx]

        while (idx < size):
            if random() <= self.crossover:
                (p1, p2) = self._selectParents()
                children = p1.mate(p2)
                for c in children:
                    if random() <= self.mutation:
                        buf.append(c.mutate())
                    else:
                        buf.append(c)
                idx += 2
            else:
                if random() <= self.mutation:
                    buf.append(self.population[idx].mutate())
                else:
                    buf.append(self.population[idx])
                idx += 1

        self._outputPatterns()

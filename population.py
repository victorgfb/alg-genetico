from DNA import DNA
from random import randint
from copy import deepcopy

class Population:
    def __init__(self, mutationRate, crossoverRate, qtd):
        self.mutationRate = mutationRate
        self.crossorverRate = crossoverRate
        self.generation = 0
        self.population = []
        self.qtd = qtd
        for i in range(qtd):
            self.population.append(DNA(4))
            self.population[i].calcFitness()
        self.populationCopy = deepcopy(self.population)

    def generate(self):
        nextGeneration = []
        partner1 = self.tornament()
        partner2 = self.tornament()
        
        for _ in range(int(self.qtd/2)):
            child1, child2 = partner1.crossover(partner2, self.crossorverRate)
            child1.mutate(self.mutationRate)
            child2.mutate(self.mutationRate)
            child1.calcFitness()
            child2.calcFitness()
            nextGeneration.append(child1)
            nextGeneration.append(child2)
            self.populationCopy = deepcopy(self.population)

        self.population = nextGeneration
        self.generation += 1

    def tornament(self):
        aux = randint(0,len(self.populationCopy) - 1)
        first = self.populationCopy.pop(aux)
        aux = randint(0,len(self.populationCopy) -1)
        second = self.populationCopy.pop(aux)
        if(first.fitness < second.fitness):
            return first
        return second

    def getBestFitness(self):
        mini = self.population[0]

        for i in range(len(self.population)):
            if(self.population[i].fitness < mini.fitness):
                mini = self.population[i]
        return mini.convert()



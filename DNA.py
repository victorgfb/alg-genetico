from random import randint
from random import uniform
from copy import deepcopy

class DNA:
    def __init__(self, tam):
        self.genes = []
        self.fitness = 0
        self.tam = tam
        for _ in range(tam):
            self.genes.append(randint(0,1))

    def calcFitness(self):
        x = self.convert()
        self.fitness =  x*x - 3*x + 4 

    def convert(self): 
        aux = deepcopy(self.genes)
        signal = aux.pop(0)
        s = [str(i) for i in aux] 
        res = "".join(s)

        if(signal):
            signal = -1
        else:
            signal = 1
        return(int(res,2) * signal)

    def crossover(self, partner, crossorverRate):
        prob = uniform(0,100)
        if( prob <= crossorverRate):
            tam = len(self.genes)
            child1 = DNA(tam)
            child2 = DNA(tam)
            midpoint = randint(0, tam)
            for i in range(tam):
                i = i - 1
                if i <= midpoint:
                    child1.genes[i] = self.genes[i]
                    child2.genes[i] = partner.genes[i]
                else:
                    child1.genes[i] = partner.genes[i]
                    child2.genes[i] = self.genes[i]
            return child1, child2
        else:
            return self, partner
            
    
    def mutate(self, mutationRate):
        for i in range(len(self.genes)):
            prob = uniform(0,100)
            if prob < mutationRate:
                self.genes[i] = int(not(self.genes[i]))
                #print("entrou")

dna = DNA(4)
dna.calcFitness()
from population import Population

population = Population(1,60,4)

while(population.generation <= 1000):
    population.generate()

print(population.getBestFitness())
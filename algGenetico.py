from population import Population

population = Population(1,60,4)

while(population.generation <= 5):
    population.generate()

print(population.getBestFitness())
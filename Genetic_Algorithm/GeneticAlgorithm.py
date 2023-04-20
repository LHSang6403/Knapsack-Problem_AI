import random

population_size = 10
mutation_probability = 0.3
generations = 100

max_weight = 0
total_label = 0
items_size = 0

weights = []
values = []
labels = []


def generate_population(population_size: int) -> list[list[int]]:
    """Function to generate a random population"""
    population = []
    for _ in range(population_size):
        genes = [0, 1]
        chromosome = []
        for _ in range(items_size):
            chromosome.append(random.choice(genes))
        population.append(chromosome)
    print("Generated a random population of size", population_size)
    return population


def calculate_fitness(chromosome: list[int]) -> int:
    """function to calculate the fitness of a chromosome"""
    total_weight = 0
    total_value = 0
    picked_label = 0
    labels_count = {}

    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_weight += weights[i]
            total_value += values[i]

    if total_weight > max_weight:
        return 0
    else:
        return total_value


def select_chromosomes(population: list[list[int]]) -> tuple[list[int], list[int]]:
    """function to select two chromosomes for crossover"""
    fitness_values = []
    for chromosome in population:
        fitness_values.append(calculate_fitness(chromosome))

    fitness_values = [float(i)/sum(fitness_values) for i in fitness_values]

    parents = random.choices(population, weights=fitness_values, k=2)

    print("Selected two chromosomes for crossover")
    return parents[0], parents[1]


def crossover(parent1: list[int], parent2: list[int]) -> tuple[list[int], list[int]]:
    """function to perform crossover between two chromosomes"""
    crossover_point = random.randint(0, items_size-1)
    child1 = parent1[0:crossover_point] + parent2[crossover_point:]
    child2 = parent2[0:crossover_point] + parent1[crossover_point:]

    print("Performed crossover between two chromosomes")
    return child1, child2

def mutate(chromosome: list[int]) -> list[int]:
    """function to perform mutation on a chromosome"""
    mutation_point = random.randint(0, items_size-1)
    if chromosome[mutation_point] == 0:
        chromosome[mutation_point] = 1
    else:
        chromosome[mutation_point] = 0
    print("Performed mutation on a chromosome")
    return chromosome


def get_best(population: list[list[int]]) -> list[int]:
    """function to get the best chromosome from the population"""
    fitness_values = []
    for chromosome in population:
        fitness_values.append(calculate_fitness(chromosome))

        max_value = max(fitness_values)
        max_index = fitness_values.index(max_value)
        return max_value, population[max_index]


def genetic(W: int, m: int, wt: list, v: list, c: list) -> tuple[int, list]:
    """
        The function performs genetic algortihm to solve Kapsnack

        Parameters:
            - W: the bag size
            - m: count of classes
            - wt: weights
            - v: values
            - c: class labels

        Returns: A tuple
            - max_val: a high-quality max value of solution
            - chosen: a list contain a set of items has sum is max_val
        """
    global max_weight, total_label, items_size, weights, values, labels
    items_size = len(v)
    max_weight = W
    total_label = m
    values = v
    weights = wt
    labels = c

    population = generate_population(population_size)
    for _ in range(generations):
        # select two chromosomes for crossover
        parent1, parent2 = select_chromosomes(population)

        # perform crossover to generate two new chromosomes
        child1, child2 = crossover(parent1, parent2)

        # perform mutation on the two new chromosomes
        if random.uniform(0, 1) < mutation_probability:
            child1 = mutate(child1)
        if random.uniform(0, 1) < mutation_probability:
            child2 = mutate(child2)

        # replace the old population with the new population
        population = [child1, child2] + population[2:]

    max_val, best = get_best(population)

    return max_val, best

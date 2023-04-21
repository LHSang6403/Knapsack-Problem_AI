import random

population_size = 100
mutation_probability = 0.3
generations = 1000

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
    return population


def calculate_fitness(chromosome: list[int]) -> int:
    """function to calculate the fitness of a chromosome"""
    total_weight = 0
    total_value = 0

    labels_count = [0] * (total_label + 1)
    labels_count[0] += 1

    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_weight += weights[i]
            total_value += values[i]
            labels_count[labels[i]] += 1

    if total_weight > max_weight:
        return int (0.1 * total_value)
    elif all(count > 0 for count in labels_count):
        return total_value
    else:
        return int(0.1 * total_value)



def select_chromosomes(population: list[list[int]]) -> tuple[list[int], list[int]]:
    """function to select two chromosomes for crossover"""
    fitness_values = []
    for chromosome in population:
        fitness_values.append(calculate_fitness(chromosome))

    fitness_values = [float(i)/sum(fitness_values) for i in fitness_values]

    parents = random.choices(population, weights=fitness_values, k=2)

    return parents[0], parents[1]


def crossover(parent1: list[int], parent2: list[int]) -> tuple[list[int], list[int]]:
    """function to perform crossover between two chromosomes"""
    crossover_point = random.randint(0, items_size-1)
    child1 = parent1[0:crossover_point] + parent2[crossover_point:]
    child2 = parent2[0:crossover_point] + parent1[crossover_point:]

    return child1, child2

def mutate(chromosome: list[int]) -> list[int]:
    """function to perform mutation on a chromosome"""
    mutation_point = random.randint(0, items_size-1)
    if chromosome[mutation_point] == 0:
        chromosome[mutation_point] = 1
    else:
        chromosome[mutation_point] = 0
    return chromosome


def get_best(population: list[list[int]]) -> list[int]:
    """function to get the best chromosome from the population"""
    fitness_values = []
    weight = 0
    for chromosome in population:
        fitness_values.append(calculate_fitness(chromosome))
    max_value = max(fitness_values)
    max_index = fitness_values.index(max_value)
    
    for i in range(items_size):
        if (population[max_index][i] == 1):
            weight += weights[i]
    if weight > max_weight:
        return 0, [0 for _ in range(items_size)]
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
    global population_size, generations
    global max_weight, total_label, items_size, weights, values, labels
    items_size = len(v)
    max_weight = W
    total_label = m
    values = v
    weights = wt
    labels = c

    population_size = items_size * 10
    generations = items_size * 100

    max_val = 0
    curr_generation = 0        
    population = generate_population(population_size)

    for _ in range(generations):
        new_population = []
        while len(new_population) < len(population):
            # select two chromosomes for crossover
            parent1, parent2 = select_chromosomes(population)

            # perform crossover to generate two new chromosomes
            child1, child2 = crossover(parent1, parent2)

            # perform mutation on the two new chromosomes
            if random.uniform(0, 1) < mutation_probability:
                child1 = mutate(child1)
            if random.uniform(0, 1) < mutation_probability:
                child2 = mutate(child2)
            new_population.append(child1)
            new_population.append(child2)
        # replace the old population with the new population
        population = new_population

    max_val, best = get_best(population)
    return max_val, best

import random
from math import sqrt

loop_count = 0

expoect_seconds = 1
expoect_calc = int(10**8/6 * expoect_seconds)
mutation_probability = 0.3
population_size = 100
generations = 1000

max_weight = 0
total_label = 0
items_size = 0

weights = []
values = []
labels = []

def calculate_fitness(chromosome: list[int]) -> tuple[bool, int]:
    """function to calculate the fitness of a chromosome
        Time complexity: O(item_size)

        Has level-0 loop
        return is_verified, fitness
    """

    global loop_count

    total_weight = 0
    total_value = 0

    labels_count = [0] * (total_label + 1)
    labels_count[0] += 1
    label_left = total_label

    for i in range(items_size):
        loop_count+=1
        
        if chromosome[i] == 1:
            total_weight += weights[i]
            total_value += values[i]
            if labels_count[labels[i]] == 0:
                label_left -= 1
            labels_count[labels[i]] += 1

        if total_weight > max_weight:
            break
        if (items_size - i - 1) < label_left:
            break

    if total_weight > max_weight or label_left > 0:
        return False, int(0.1 * total_value)
    else:
        return True, total_value


def generate_population(minimun:list[int], population_size: int) -> tuple [list[int], list[tuple[int, list[int]]]]:
    """Function to generate a random population
    
    Has level-1 loop
    Time complexity O (population_size * items_size)
    Return: total_fitness, population
    """
    global loop_count, max_weight

    population = []
    fitness_cum = []

    total_fitness = 0
    genes = [0, 1]

    init_weight = 0
    init_fitness = 0

    for i in range(items_size):
        if minimun[i] == 1:
            init_weight += weights[i]
            init_fitness += values[i]

    for _ in range (population_size):
        chromosome = minimun.copy()
        total_weight = init_weight
        fitness_value = init_fitness

        for i in range(items_size):
            if chromosome[i] == 1:
                continue

            loop_count += 1
            chromosome[i] = random.choice(genes)

            if total_weight + chromosome[i] * weights[i] > max_weight:
                break

            total_weight += weights[i] * chromosome[i]
            fitness_value += values[i] * chromosome[i]

        total_fitness += fitness_value
        population.append((fitness_value, chromosome))
        fitness_cum.append(total_fitness)

    return fitness_cum, population


def generate_satisfied_chromosome() -> tuple[int, list[int]]:
    """Generate the minimum correct answer

    Has level-0 loop
    Time complexity: O (items_size)
    Return: minimum correct fitness, minimum correct choice
    """
    global loop_count

    mini_labes = [-1] * (total_label + 1)
    chromosome = [0] * items_size

    for i in range(items_size):
        loop_count += 1
        if mini_labes[labels[i]] < 0 or weights[mini_labes[labels[i]]] > weights[i]:
            mini_labes[labels[i]] = i
    
    for pos in mini_labes:
        loop_count += 1
        chromosome[pos] = 1

    verified, fitness_value = calculate_fitness(chromosome)

    if not verified:
        return 0, []
    
    return fitness_value, chromosome

def select_chromosomes(fitness_cum: list[int], population: list[tuple[int, list[int]]]) -> tuple[list[int], list[int]]:
    """function to select two chromosomes for crossover
    
    Time complexity: O (1)
    """
    parents = random.choices(population, cum_weights=fitness_cum, k=2)
    return parents[0], parents[1]


def crossover(parent1: tuple[int, list[int]], parent2: tuple[int, list[int]]) -> tuple[list[int], list[int]]:
    """function to perform crossover between two chromosomes
    
    Time complexity: O (item_size)
    """
    crossover_point = random.randint(0, items_size-1)

    child1 = parent1[1][0:crossover_point] + parent2[1][crossover_point:]
    child2 = parent2[1][0:crossover_point] + parent1[1][crossover_point:]

    return child1, child2


def mutate(chromosome: list[int]) -> list[int]:
    """function to perform mutation on a chromosome
    
    Time complexity O(1)
    """
    mutation_point = random.randint(0, items_size-1)
    if chromosome[mutation_point] == 0:
        chromosome[mutation_point] = 1
    else:
        chromosome[mutation_point] = 0
    return chromosome

def genetic(W: int, m: int, wt: list, v: list, c: list) -> tuple[int, list]:
    """
        The function performs genetic algortihm to solve Kapsnack

        Parameters:
            - W: the bag size
            - m: count of classes
            - wt: weights
            - v: values
            - c: class labels

        Time Complexity: O(generations * populationn_size * item_size * total_label)

        Returns: A tuple
            - max_val: a high-quality max value of solution
            - chosen: a list contain a set of items has sum is max_val
        """
    global population_size, generations, loop_count
    global max_weight, total_label, items_size, weights, values, labels
    items_size = len(v)
    max_weight = W
    total_label = m
    values = v
    weights = wt
    labels = c

    print("population:", population_size, ";generations:", generations)

    max_val, best = generate_satisfied_chromosome()
    if (max_val == 0):
        return loop_count, 0, [0] * items_size

    fitness_cum, population = generate_population(best, population_size)

    for _ in range(generations):
        new_population = []
        new_fitness_cum = []
        total_fitness = 0
        while len(new_population) < len(population):

            # select two chromosomes for crossover
            parent1, parent2 = select_chromosomes(fitness_cum, population)

            # perform crossover to generate two new chromosomes
            child1, child2 = crossover(parent1, parent2)

            # perform mutation on the two new chromosomes
            if random.uniform(0, 1) < mutation_probability:
                child1 = mutate(child1)
            if random.uniform(0, 1) < mutation_probability:
                child2 = mutate(child2)
            
            verified, fitness = calculate_fitness(child1)
            if verified:
                new_population.append((fitness, child1))
                total_fitness += fitness
                new_fitness_cum.append(total_fitness)
                verified, fitness = calculate_fitness(child1)
                if fitness > max_val:
                    best = child1
                    max_val = fitness
            if verified:
                new_population.append((fitness, child2))
                total_fitness += fitness
                new_fitness_cum.append(total_fitness)
                if fitness > max_val:
                    best = child2
                    max_val = fitness


        # replace the old population with the new population
        population = new_population
        fitness_cum = new_fitness_cum

    return loop_count, max_val, best

import random
from math import sqrt

loop_count = 0

expoect_seconds = 1
expoect_calc = int(10**8/6 * expoect_seconds)
mutation_probability = 0.2

max_weight = 0
total_label = 0
items_size = 0

weights = []
values = []
labels = []

def calculate_fitness(chromosome: list[int]) -> tuple[int, int, int]:
    """function to calculate the fitness of a chromosome
        Time complexity: O(item_size * total_label)
    """

    global loop_count

    total_weight = 0
    total_value = 0

    labels_count = [0] * (total_label + 1)
    labels_count[0] += 1
    label_left = total_label

    for i in range(len(chromosome)):
        loop_count+=1
        if chromosome[i] == 1:
            total_weight += weights[i]
            total_value += values[i]
            if labels_count[labels[i]] == 0:
                label_left -= 1
            labels_count[labels[i]] += 1

    if total_weight > max_weight:
        return total_weight - max_weight, label_left, int(0.1 * total_value)
    elif label_left == 0:
        return 0, 0, total_value
    else:
        return 0, label_left, int(0.1 * total_value)


def generate_population(population_size: int) -> tuple[int, list[tuple[int, list[int]]]]:
    """Function to generate a random population
    
    Time complexity O (population_size * items_size * total_label)
    Return: total_fitness, population
    """
    global loop_count

    population = []

    total_fitness = 0
    time_try = population_size
    genes = [0, 1]

    while time_try > 0 and len(population) < population_size:
        if time_try == 0 and len(population) == 0:
            return 0, []
        
        chromosome = []
        for _ in range(items_size):
            loop_count += 1
            chromosome.append(random.choice(genes))
        weight_diff, class_left, fitness_value = calculate_fitness(chromosome)
        if time_try > 0 and (weight_diff > 0 or class_left > 0):     
            time_try -= 1  
            continue
        population.append((fitness_value, chromosome))
        total_fitness += fitness_value

    return total_fitness, population


def generate_satisfied_chromosome() -> tuple[int, list[int]]:
    """Generate the minimum correct answer

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

    weight_diff, class_left, fitness_value = calculate_fitness(chromosome)
    if weight_diff > 0 or class_left > 0:
        return 0, []
    
    return fitness_value, chromosome

def select_chromosomes(fitness_rate: list[int], population: list[tuple[int, list[int]]]) -> tuple[list[int], list[int]]:
    """function to select two chromosomes for crossover
    
    Time complexity: O (1)
    """
    parents = random.choices(population, weights=fitness_rate, k=2)
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

    population_size = 100
    generations = (expoect_calc - items_size - population_size * items_size * total_label - population_size * 2)/(population_size + population_size)

    print("population:", population_size, "generations:", generations, "total:", population_size * generations)

    max_val, best = generate_satisfied_chromosome()
    if (max_val == 0):
        return loop_count, 0, [0] * items_size

    total_fitness, population = generate_population(population_size - 1)

    if total_fitness == 0:
        total_fitness = max_val * population_size
        population = [(max_val, best)] * population_size

    if len(population) < population_size:
        loop_count += 1
        total_fitness += max_val * (population_size - len(population))
        population += [(max_val, best)] * (population_size - len(population))

    fitness_rate = []
    for item in population:
        loop_count += 1
        fitness_rate.append(item[0])

    for _ in range(generations):
        new_population = []
        while len(new_population) < len(population):
            # select two chromosomes for crossover
            parent1, parent2 = select_chromosomes(fitness_rate, population)

            # perform crossover to generate two new chromosomes
            child1, child2 = crossover(parent1, parent2)

            # perform mutation on the two new chromosomes
            if random.uniform(0, 1) < mutation_probability:
                child1 = mutate(child1)
            if random.uniform(0, 1) < mutation_probability:
                child2 = mutate(child2)
            loop_count += 1
            new_population.append(child1)
            new_population.append(child2)

        # replace the old population with the new population

        population.clear()
        fitness_rate.clear()

        total_fitness = 0
        for item in new_population:
            weight_diff, class_left, fitness_value = calculate_fitness(item)
            if fitness_value > max_val and weight_diff == 0 and class_left == 0:
                best = item
                max_val = fitness_value
            population.append((fitness_value, item))
            fitness_rate.append(fitness_value)
            total_fitness += fitness_value

    return loop_count, max_val, best

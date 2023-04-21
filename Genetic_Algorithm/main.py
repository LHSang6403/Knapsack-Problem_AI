import numpy as np
from timeit import default_timer as timer
import os
import sys

current_directory = os.path.dirname(
    os.path.dirname(os.path.realpath(__file__)))
sys.path.append(current_directory)


from GeneticAlgorithm import (
    genetic
)
from DoFile import *

from checkValid import (
    checkValid
)

for i in range(1,9):
# Read input data
    input_file = os.path.join(current_directory, "INPUT_" + str(i) + ".txt")
    knapsack_capacity, num_classes, weights, values, class_labels = read_input(
        input_file)

    print(input_file)
    print("Capacity:", knapsack_capacity)
    print("Num classes: ", num_classes)
    print(len(weights), " items")

    start_time = timer()
    # Solve knapsack problem using local beam search
    best_value, best_solution = genetic(
        knapsack_capacity, num_classes, weights, values, class_labels)
    end_time = timer()
    print("Solution:", best_value)
    print("Time using:", round (end_time - start_time, 4), "seconds")
    print("Valid status:", checkValid(knapsack_capacity,
            num_classes, weights, values, class_labels, best_solution))
    print()
    # Write output data
    output_file = os.path.join(
        current_directory, "Genetic_Algorithm", "OUTPUT_" + str(i) + ".txt")
    write_output(output_file, best_value, best_solution)
print("\nAlgoritm end!")
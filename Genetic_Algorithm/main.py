import numpy as np
import os
import sys

current_directory = os.path.dirname(
    os.path.dirname(os.path.realpath(__file__)))
sys.path.append(current_directory)

from GeneticAlgorithm import (
    genetic
)
from DoFile import *


for i in range(1,9):
# Read input data
    input_file = os.path.join(current_directory, "INPUT_" + str(i) + ".txt")
    knapsack_capacity, num_classes, weights, values, class_labels = read_input(
        input_file)

    print(input_file)
    print("Capacity:", knapsack_capacity)
    print("Num classes: ", num_classes)
    print(len(weights), " items")
    # Solve knapsack problem using local beam search
    best_value, best_solution = genetic(
        knapsack_capacity, num_classes, weights, values, class_labels)

    print("Solution:", best_value)
    print()
    # Write output data
    output_file = os.path.join(
        current_directory, "Genetic_Algorithm", "OUTPUT_" + str(i) + ".txt")
    write_output(output_file, best_value, best_solution)
print("\nAlgoritm end!")
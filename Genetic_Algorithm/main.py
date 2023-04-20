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



# Read input data
input_file = os.path.join(current_directory, "INPUT_3.txt")
knapsack_capacity, num_classes, weights, values, class_labels = read_input(
    input_file)

# Set algorithm parameters
beam_width = 100
max_iter = 1000

# Solve knapsack problem using local beam search
best_value, best_solution = genetic(
    knapsack_capacity, num_classes, weights, values, class_labels)

# Write output data
output_file = os.path.join(
    current_directory, "Genetic_Algorithm", "OUTPUT_3.txt")
write_output(output_file, best_value, best_solution)

print("\nGenetic algorithm finished")

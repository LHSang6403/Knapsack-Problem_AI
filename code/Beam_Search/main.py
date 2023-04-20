import numpy as np
from Beam_Search import (
    local_beam_search
)
from DoFile import *
import os
import sys
import random

current_directory = os.getcwd()
sys.path.append(current_directory)


# main function


def main():
    # Read input data
    input_file = os.path.join(current_directory, "INPUT_1.txt")
    knapsack_capacity, num_classes, weights, values, class_labels = read_input(
        input_file)

    # Set algorithm parameters
    n = len(weights)
    if n in range(0, 10):
        beam_width = 100
    elif n in range(11, 50):
        beam_width = 5000
    elif n in range(51, 100):
        beam_width = 10000
    elif n in range(101, 1000):
        beam_width = 10000 * (n/100)
    # Solve knapsack problem using local beam search
    best_value, best_solution = local_beam_search(
        knapsack_capacity, num_classes, weights, values, class_labels, beam_width)
    # Write output data
    output_file = os.path.join(
        current_directory, "Beam_Search", "OUTPUT_1.txt")
    write_output(output_file, best_value, best_solution)

    print("\nBeam search finished")


if __name__ == '__main__':
    # code to execute when the file is run as the main program
    # e.g., calling the main function
    main()

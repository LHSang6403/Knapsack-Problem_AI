import numpy as np
import os
import sys
import random

current_directory = os.getcwd()
sys.path.append(current_directory)

from DoFile import *

from Beam_Search import (
    local_beam_search
)


# main function


def main():
    # Read input data
    input_file = os.path.join(current_directory, "INPUT_10.txt")
    knapsack_capacity, num_classes, weights, values, class_labels = read_input(
        input_file)

    beam_width = 1000
    # Set algorithm parameters
    # Solve knapsack problem using local beam search
    best_value, best_solution = local_beam_search(
        knapsack_capacity, num_classes, weights, values, class_labels, beam_width)
    # Write output data
    output_file = os.path.join(
        current_directory, "Beam_Search", "OUTPUT_10.txt")
    write_output(output_file, best_value, best_solution)

    print("\nBeam search finished")


if __name__ == '__main__':
    # code to execute when the file is run as the main program
    # e.g., calling the main function
    main()

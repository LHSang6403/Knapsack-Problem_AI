import os
import sys

current_directory = os.getcwd()
sys.path.append(current_directory)

from DoFile import *
from Beam_Search import (
    local_beam_search
)
import numpy as np
import os



# main function


def main():
    # Read input data
    input_file = current_directory + '\INPUT_4.txt'
    knapsack_capacity, num_classes, weights, values, class_labels = read_input(
        input_file)

    # Set algorithm parameters
    beam_width = 100
    max_iter = 2000

    # Solve knapsack problem using local beam search
    best_value, best_solution = local_beam_search(
        knapsack_capacity, num_classes, weights, values, class_labels, beam_width, max_iter)

    # Write output data
    output_file = current_directory + '\Beam_Search\OUTPUT_4.txt'
    write_output(output_file, best_value, best_solution)

    print("\nBeam search finished")

if __name__ == '__main__':
    # code to execute when the file is run as the main program
    # e.g., calling the main function
    main()

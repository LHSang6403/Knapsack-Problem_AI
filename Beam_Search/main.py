import numpy as np
import os

from DoFile import (
    read_input,
    write_output,
)

from Beam_Search import (
    local_beam_search
)

# main function


def main():
    # Read input data
    input_file = 'D:\CODE\Python\Knap-Sack_Problem\INPUT_1.txt'
    knapsack_capacity, num_classes, weights, values, class_labels = read_input(
        input_file)

    # Set algorithm parameters
    beam_width = 100
    max_iter = 1000

    # Solve knapsack problem using local beam search
    best_value, best_solution = local_beam_search(
        knapsack_capacity, num_classes, weights, values, class_labels, beam_width, max_iter)

    # Write output data
    output_file = 'D:\CODE\Python\Knap-Sack_Problem\OUTPUT_1.txt'
    write_output(output_file, best_value, best_solution)


if __name__ == '__main__':
    # code to execute when the file is run as the main program
    # e.g., calling the main function
    main()

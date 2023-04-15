import os
import sys

current_directory = os.getcwd()
sys.path.append(current_directory)

from DoFile import *
from BruteForceSearching import (
    brute_force
)
import numpy as np
import os



# main function


def main():
    # Read input data
<<<<<<< HEAD
    input_file = current_directory + '\INPUT_1.txt'
=======
    input_file = current_directory + '\INPUT_4.txt'
>>>>>>> 08799e92a0d8fe93904b69aa925b1fb961bc0654
    knapsack_capacity, num_classes, weights, values, class_labels = read_input(
        input_file)

    # Set algorithm parameters
    beam_width = 100
    max_iter = 2000

    # Solve knapsack problem using local beam search
    best_value, best_solution = brute_force(
        knapsack_capacity, num_classes, weights, values, class_labels)

    # Write output data
<<<<<<< HEAD
    output_file = current_directory + '\Brute_Force\OUTPUT_1.txt'
    write_output(output_file, best_value, best_solution)

    print("\nBeam search finished")
=======
    output_file = current_directory + '\Brute_Force\OUTPUT_4.txt'
    write_output(output_file, best_value, best_solution)

    print("\nBrute Force search finished")
>>>>>>> 08799e92a0d8fe93904b69aa925b1fb961bc0654

if __name__ == '__main__':
    # code to execute when the file is run as the main program
    # e.g., calling the main function
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 08799e92a0d8fe93904b69aa925b1fb961bc0654

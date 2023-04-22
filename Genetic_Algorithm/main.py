import numpy as np
from timeit import default_timer as timer
import os
import sys

current_directory =  os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(current_directory))


from GeneticAlgorithm import (
    genetic
)
from DoFile import *

from checkValid import (
    checkValid
)

log = open(os.path.join(current_directory, "log.txt"), "w")
log.write("Starting here!!!\n")

for i in range(1,12):
# Read input data
    input_file = os.path.join(os.path.dirname(current_directory), "INPUT_" + str(i) + ".txt")
    knapsack_capacity, num_classes, weights, values, class_labels = read_input(
        input_file)

    print(input_file)
    print("Capacity:", knapsack_capacity)
    print("Num classes: ", num_classes)
    print(len(weights), "items")

    log.write(input_file + "\n")
    log.write("Capacity: " + str(knapsack_capacity) + "\n")
    log.write("Num classes: " + str(num_classes) + "\n")
    log.write(str(len(weights)) + " items\n")
    log.flush()

    start_time = timer()
    # Solve knapsack problem using local beam search
    loop, best_value, best_solution = genetic(
        knapsack_capacity, num_classes, weights, values, class_labels)
    end_time = timer()
    
    print("Solution:", best_value)
    print("Loop count:", loop)
    print("Time using:", round (end_time - start_time, 4), "seconds")
    print("Valid status:", checkValid(knapsack_capacity,
            num_classes, weights, values, class_labels, best_solution))
    print()

    log.write("Solution: " + str(best_value) + "\n")
    log.write("Loop count: " + str(loop) + "\n")
    log.write("Time using: " +
              str(round(end_time - start_time, 4)) + " seconds" + "\n")
    log.write("Valid status: " + str(checkValid(knapsack_capacity,
                                                num_classes, weights, values, class_labels, best_solution)) + "\n")
    log.write("\n")
    log.flush()

    # Write output data
    output_file = os.path.join(current_directory, "OUTPUT_" + str(i) + ".txt")
    write_output(output_file, best_value, best_solution)
print("\nAlgorithm end!")
log.close()
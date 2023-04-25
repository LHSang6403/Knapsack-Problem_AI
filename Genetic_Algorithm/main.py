import matplotlib.pyplot as plt
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

plt.ioff()

generation_init = 10
counting = 10
step = 10

for i in range(1,12):

    figure, axis = plt.subplots(2, 1)
    plt.close(figure)
    ## figure.set_dpi(200)
    figure.tight_layout(pad=2)
    figure.text(0.5, 0.04, "Generations", ha='center', va='center')

    # Read input data

    generations = []
    times = []
    ans = []

    generation_count = generation_init
    input_file = os.path.join(os.path.dirname(current_directory), "INPUT_" + str(i) + ".txt")
    knapsack_capacity, num_classes, weights, values, class_labels = read_input(
        input_file)
    
    chart = open(os.path.join(
        current_directory, "CHART_" + str(i) + ".csv"), "w")
    
    chart.write("Generations, Loop, Times (miliseconds), Answer\n")
    chart.flush()
    
    for _ in range(counting + 1):
        print("INPUT_" + str(i) + ".txt")
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
            generation_count, knapsack_capacity, num_classes, weights, values, class_labels)
        end_time = timer()
        
        chart.write(str(generation_count) + "," +str(loop) + "," + str(int(round(1000*(end_time - start_time), 0))) + "," + str(best_value) + "\n")
        chart.flush()

        generations.append(generation_count)
        times.append(int(round(1000*(end_time - start_time), 0)))
        ans.append(best_value)

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
        generation_count += step

    # Write output data
    output_file = os.path.join(current_directory, "OUTPUT_" + str(i) + ".txt")
    write_output(output_file, best_value, best_solution)
    chart.close()

    info = "Test_" + str(i) + " - items: " + str(len(weights)) + " - class: " + str(num_classes)


    axis[0].set_title("Miliseconds " + info)
    axis[1].set_title("Answers " + info)

    axis[0].plot(generations, times)
    axis[0].scatter(generations, times)

    for id, txt in enumerate(times):
        axis[0].annotate(txt, (generations[id]+30, times[id]+30))

    axis[1].plot(generations, ans)
    axis[1].scatter(generations, ans)
    for id, txt in enumerate(ans):
        axis[1].annotate(txt, (generations[id]+.3, ans[id]+.3))

    figure.savefig(os.path.join(
        current_directory, "CHART_" + str(i) + ".png"))

print("\nAlgorithm end!")
log.close()
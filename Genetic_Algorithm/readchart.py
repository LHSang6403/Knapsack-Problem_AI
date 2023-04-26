import matplotlib.pyplot as plt
import matplotx
import os

start = 2
limit = 6
pwd = os.path.dirname(os.path.realpath(__file__))
values = {}
generations = []
population = [30, 15, 30, 90, 135, 120, 375, 900, 2100, 6000, 15000]
items_size = [10, 5, 10, 20, 30, 40, 50, 100, 200, 500, 1000]
indexes = []

output = open(os.path.join(pwd, "small-value.csv"), "w")

output.write("Items_size, ")
for i in range (start - 1, len(items_size)):
    output.write(str(items_size[i]) + ",")

output.write("\nPopulation, ")
for i in range(start - 1, len(population)):
    output.write(str(population[i]) + ",")
output.write("\n")


for value in range (start,limit + 1):
    values[value] = []
    indexes.append(value)
    with open (os.path.join(pwd, "CHART_" + str(value) + ".csv"), "r") as file:
        for line in file:
            if line[0] != 'G':
                
                values[value].append(int(line.split(",")[3]))

                if value == start:
                    generations.append(int(line.split(",")[0]))


output.flush()
for i, gen in enumerate(generations):
    output.write(str(gen) + ",")
    for value in values.items():
        if  len(value[1]) <= 0:
            continue
        output.write(str(value[1][i]) + ",")
    output.write("\n")
output.flush()

for i, value in enumerate(values.items()):
    if len(value[1]) == 0:
        continue
    plt.plot(generations, value[1], label="Size_" + str(items_size[indexes[i] - 1]))
    plt.scatter(generations, value[1])

plt.ylabel("Max total value")
plt.xlabel("Generation")
plt.legend(loc="best")
plt.title("Small dataset")
plt.savefig(os.path.join(pwd, "small-value.png"))

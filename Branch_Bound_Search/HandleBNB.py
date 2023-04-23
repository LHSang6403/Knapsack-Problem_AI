import BranchBoundSearching
import numpy as np
import datetime

def ReadFile(fileInput):
    BNB = BranchBoundSearching.Problem() 

    data = open(f"{fileInput}", "r")
    lines = data.readlines()

    BNB._capacity = float(lines[0])
    BNB._numOfClass = int(lines[1])
    weights = np.array(list(map(float, lines[2].replace("\n", "").split(", "))))
    values = np.array(list(map(float, lines[3].replace("\n", "").split(", "))))
    BNB._classLabel = np.array(list(map(int, lines[4].replace("\n", "").split(", "))))
    delta = values/weights

    for i in range(len(values)):
        node = BranchBoundSearching.Node(weights[i], values[i], delta[i], i)
        BNB._data.append(node)
    BNB._data = np.sort(BNB._data)

    return BNB

def WriteFile(fileOutput, BNB):
    output_file = open(f"{fileOutput}", "w")
    output_file.write(f"{BNB._maxVal}\n")
    if BNB._maxVal == 0:
        output_file.write("Can not solve")
    else:
        output_file.write(f"{BNB._answer}".replace('[', '').replace(']', '') + "\n")
    output_file.close()

def SolveKnapsackUsingBNB(BNB, fileInput, fileOutput):
    print("Start")
    BNB = ReadFile(fileInput)
    startTime = datetime.datetime.now()

    # This code initializes a 1D numpy array arr with zeros
    # The length of the array is set to the number of items in self._data
    arr = np.array([0] * len(BNB._data))
    print("Processing...")
    BNB.BranchAndBound(BNB._data, arr, 0, 0, BNB._capacity)
    endTime = datetime.datetime.now()
    executionTime = (endTime - startTime).total_seconds()

    WriteFile(fileOutput, BNB)
    print(f"Done: {executionTime} s")
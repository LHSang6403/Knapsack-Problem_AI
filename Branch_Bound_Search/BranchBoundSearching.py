import numpy as np
import time
import os
import tracemalloc

class Node:
    def __init__(self, weight, value, delta, index):
        self._weight = weight
        self._value = value
        self._delta = delta
        self._index = index
    def __lt__(self, node):
        return self._delta > node._delta

class Solving:
    def __init__(self, fileInput, fileOutput):
        self._maxVal = 0
        self._answer = []
        self._capaticy = 0
        self._numOfClass = 0
        self._classLabel = None
        self._data = []
        self._fileInput = fileInput
        self._fileOutput = fileOutput

    def GetData(self):
        dataset_file = open(f"{self._fileInput}", "r")
        lines = dataset_file.readlines()

        self._capacity = float(lines[0])
        self._numOfClass = int(lines[1])
        weights = np.array(list(map(float, lines[2].replace("\n", "").split(", "))))
        values = np.array(list(map(float, lines[3].replace("\n", "").split(", "))))
        self._classLabel = np.array(list(map(int, lines[4].replace("\n", "").split(", "))))
        delta = values/weights

        for i in range(len(values)):
            node = Node(weights[i], values[i], delta[i], i)
            self._data.append(node)
        self._data = np.sort(self._data)

    def PrintResult(self):
        output_file = open(f"{self._fileOutput}", "w")
        output_file.write(f"{self._maxVal}\n")
        if self._maxVal == 0:
            output_file.write("No optimal solution found!")
        else:
            output_file.write(f"{self._answer}".replace('[', '').replace(']', '') + "\n")
        output_file.close()

    def SolveKnapsackUsingBNB(self):
        self.GetData()
        arr = np.array([0] * len(self._data))
        self.BranchAndBound(self._data, arr, 0, 0, self._capacity)
        self.PrintResult()

    def CopyArray(self, arr):
        other = []
        for i in arr:
            other.append(i)
        self._answer = other

    def checkClass(self, arr):
        classExist = []
        temp = np.where(arr == 1)
        for i in temp[0]:
            classExist.append(self._classLabel[i])
        for i in range(self._numOfClass):
            if i + 1 not in classExist:
                return False
        return True

    def BranchAndBound(self, nodes, arr, id, curVal, curWeight):
        i = 1
        while i >= 0:
            arr[nodes[id]._index] = i
            curV = curVal + nodes[id]._value * i
            curW = curWeight - nodes[id]._weight * i
            if id == len(self._data) - 1:
                if i == 1:
                    if curW >= 0:
                        if curV > self._maxVal and self.checkClass(arr):
                            self._maxVal = curV
                            self.CopyArray(arr)
                        return
                else:
                    if curV > self._maxVal and self.checkClass(arr):
                        self._maxVal = curV
                        self.CopyArray(arr)
                    return
            else:
                g = curV + curW * nodes[id + 1]._delta
                if i == 1:
                    if curW >= 0 and g > self._maxVal:
                        self.BranchAndBound(nodes, arr, id + 1, curV, curW)
                else:
                    if g > self._maxVal:
                        self.BranchAndBound(nodes, arr, id + 1, curV, curW)
                    return
            i -= 1

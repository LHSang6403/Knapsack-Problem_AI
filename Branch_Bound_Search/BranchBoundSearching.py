import numpy as np
import sys
sys.setrecursionlimit(10000) # solve recursive error

class Node:
    def __init__(self, weight, value, delta, index):
        self._weight = weight
        self._value = value
        self._delta = delta
        self._index = index

    def __lt__(self, node):
        return self._delta > node._delta

class Problem:
    def __init__(self):
        self._maxVal = 0
        self._answer = []
        self._capaticy = 0
        self._numOfClass = 0
        self._classLabel = None
        self._data = []

    def CopyArray(self, arr):
        other = []
        for i in arr:
            other.append(i)
        self._answer = other

    def CheckClass(self, arr):
        classExist = []

        #The np.where() function returns the indices of elements in an array 
        # that meet a certain condition
        #In this case, it returns a tuple containing an array temp that 
        # holds the indices where the values in arr are equal to 1
        temp = np.where(arr == 1)

        for i in temp[0]:
            classExist.append(self._classLabel[i])
        for i in range(self._numOfClass):
            if i + 1 not in classExist:
                return False
        return True

    # nodes: a list of Node objects representing the items in the knapsack problem
    # arr: a binary array indicating which items are currently in the knapsack (1 for in, 0 for out)
    # id: the index of the current node being considered
    # curVal: the current value of the items in the knapsack
    # Formula: g = v + w(vi+1 / wi+1), w is remaining weight
    def BranchAndBound(self, nodes, arr, id, curVal, curWeight):
        i = 1 # 1 is left child, 0 is right child
        while i >= 0:
            arr[nodes[id]._index] = i

            ## Total value of the knapsack after considering the current node
            curV = curVal + nodes[id]._value * i # total value
            curW = curWeight - nodes[id]._weight * i # remaining weight

            if id == len(self._data) - 1: # considering the last node
                if i == 1: # left child
                    if curW >= 0:
                        if curV > self._maxVal and self.CheckClass(arr):
                            self._maxVal = curV
                            self.CopyArray(arr)
                        return
                else: #right child
                    if curV > self._maxVal and self.CheckClass(arr):
                        self._maxVal = curV
                        self.CopyArray(arr)
                    return
            else: # isn't the last node
                g = curV + curW * nodes[id + 1]._delta
                if i == 1: #left child
                    if curW >= 0 and g > self._maxVal:
                        self.BranchAndBound(nodes, arr, id + 1, curV, curW)
                    #else: switch to i = 0 at the next loop (i = 0)
                else: #right child
                    if g > self._maxVal:
                        self.BranchAndBound(nodes, arr, id + 1, curV, curW)
                    return
            i -= 1
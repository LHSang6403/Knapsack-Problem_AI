with open('/Users/lehoangsang/coding/Knapsack_Problem_AI/INPUT_1.txt', 'r') as f:
    lines = f.readlines()

n = int(lines[0])
k = int(lines[1])
arr = [[int(x) for x in line.split(',')] for line in lines[2:]]

print(n)
print(k)
print(arr)
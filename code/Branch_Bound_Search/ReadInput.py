def ReadInput(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()

    n = int(lines[0])
    k = int(lines[1])
    arr = [[int(x) for x in line.split(',')] for line in lines[2:]]

    return n, k, arr
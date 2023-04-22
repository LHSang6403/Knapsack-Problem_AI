def checkValid(W: int, m: int, wt: list, v: list, c: list, solution: list) -> bool:
    weight = 0
    labels = [0] * (m + 1)
    label_left = m

    for i in range(len(solution)):
        if (solution[i] == 1):
            if (labels[c[i]] == 0):
                label_left -= 1
            labels[c[i]] += 1
            weight += wt[i]

    if (label_left == 0) and (weight <= W):
        return True
    else:
        return False

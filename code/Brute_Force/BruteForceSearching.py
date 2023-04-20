import itertools


def checkCountClass(count_class):
    for i in range(len(count_class)):
        if count_class[i] <= 0:
            return False
    return True
def brute_force(W, m, wt, v, c):
    max_val = 0
    n = len(wt)
    count_class = [0 for i in range(m)]
    chosen = [0 for i in range(n)]
    all_combinations = [[0,1] for i in range(n)]
    counter = 0
    for temp in itertools.product(*all_combinations):
        counter+=1
        print(counter)
        count_class[:] = [0 for i in count_class]
        value = 0
        weight = 0
        for i in range(len(temp)):
            if weight > W:
                break
            value += temp[i] * v[i]
            weight += temp[i] * wt[i]
        for i in range(len(count_class)):
                for j in range(len(chosen)):
                    if (temp[j]==1):
                        if (c[j]==i+1):
                            count_class[i]+=1 # mảng đếm số lượng từng class
        if checkCountClass(count_class) == True:
            if weight <= W and value > max_val:
                for i in range(len(wt)):
                    chosen[i] = temp[i]
                max_val = value
    return max_val, chosen
#  0 1 

            
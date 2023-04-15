import itertools
def checkCountClass(count_class):
    for i in range(len(count_class)):
        if count_class[i] == 0:
            return False
        else:
            return True
def brute_force(W, m, wt, v, c):
    max_val = 0
    n = len(wt)
    count_class = [0 for i in range(m)]
    chosen = [0 for i in range(n)]
    all_combinations = [[0,1] for i in range(n)]
    check_count = True
    for temp in itertools.product(*all_combinations):
        check_count = True
        count_class[:] = [0 for i in count_class]
        value = 0
        weight = 0
        for i in range(len(c)):
            if weight > W:
                break
            value += temp[i] * v[i]
            weight += temp[i] * wt[i]
        for i in range(len(count_class)):
                for j in range(len(chosen)):
                    if (temp[j]==1):
                        if (c[j]==i+1):
                            count_class[i]+=1 # mảng đếm số lượng từng class
<<<<<<< HEAD
        if weight <= W and value > max_val and checkCountClass(count_class) == True:
            for i in range(len(wt)):
                chosen[i] = temp[i]
            max_val = value
=======
        if checkCountClass(count_class) == True:
            if weight <= W and value > max_val:
                for i in range(len(wt)):
                    chosen[i] = temp[i]
                max_val = value
>>>>>>> 08799e92a0d8fe93904b69aa925b1fb961bc0654
    return max_val, chosen
#  0 1 

            
import numpy as np
import itertools

# === Tính toán giá trị của một giải pháp ===
# + Nếu tổng trọng lượng các item lớn hơn trọng lượng của Knapsack:
#    => Thì giải pháp không hợp lệ và trả về -1.
# + Nếu mỗi loại item đều không có ít nhất một item được chọn:
#    => Thì trả về -1.
# + Nếu giải pháp hợp lệ:
#    => Thì trả về tổng giá trị của các item được chọn.

# evaluate a solution


def evaluate_solution(W, w, v, c, x):
    if np.sum(w * x) > W:
        return -1  # invalid solution
    val = np.sum(v * x)
    for j in range(1, c.max()+1):
        if np.sum(v[c == j] * x[c == j]) == 0:
            # invalid solution (at least one item from each class must be selected)
            return -1
    return val

 # === Tạo ra k trạng thái ban đầu ngẫu nhiên ===
 # Mỗi trạng thái là một vector n phần tử với các giá trị 0 hoặc 1.

# generate initial states (randomly)


def generate_initial_states(n, k):
    states = np.zeros((k, n), dtype=int)
    for i in range(k):
        states[i] = np.random.randint(2, size=n)
    return states

def generate_all_states(n, k):
    all_states = np.array(list(itertools.product([0, 1], repeat=n)))
    return all_states[:k]

# === Tạo ra các trạng thái con ===
# Bằng cách đảo ngược một số bit trong trạng thái đầu vào.
# Tổng số trạng thái con là n*k.

# generate descendant states by flipping some bits



def generate_descendants(states, n, k):
    descendants = np.zeros((k*n, n), dtype=int)
    for i in range(k):
        for j in range(n):
            descendants[i*n+j] = np.copy(states[i])
            descendants[i*n+j, j] = 1 - descendants[i*n+j, j]
    return descendants

# === Chọn k trạng thái tốt nhất dựa trên hàm mục tiêu ===
# Hàm mục tiêu ở đây là giá trị của giải pháp.

# select the best k states according to the objective function


def select_best_states(W, w, v, c, states, k):
    values = np.zeros(k)
    for i in range(k):
        values[i] = evaluate_solution(W, w, v, c, states[i])
    best_indices = np.argsort(values)[::-1][:k]  # indices of k best states
    return states[best_indices]

# === Thực hiện thuật toán tìm kiếm địa phương Beam Search ===
# Hàm trả về giá trị và trạng thái của giải pháp tốt nhất tìm được.

# local beam search algorithm


def local_beam_search(W, m, w, v, c, k, max_iter):
    n = len(w)  # Get the size of w
    states = generate_initial_states(n, k)
    # states = np.zeros(n, dtype=int)
    # states = generate_all_states(n, k)
    best_state = np.zeros(n, dtype=int)
    best_val = -1
    for iter in range(max_iter):
        descendants = generate_descendants(states, n, k)
        best_states = select_best_states(W, w, v, c, descendants, k)
        for i in range(k):
            val = evaluate_solution(W, w, v, c, best_states[i])
            if val > best_val:
                best_state = np.copy(best_states[i])
                best_val = val
        states = best_states
    return best_val, best_state

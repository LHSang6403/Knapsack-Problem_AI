import numpy as np
import itertools

# === Tính toán giá trị của một giải pháp ===
# + Nếu tổng trọng lượng các item lớn hơn trọng lượng của Knapsack:
#    => Thì giải pháp không hợp lệ và trả về 0.
# + Nếu mỗi loại item đều không có ít nhất một item được chọn:
#    => Thì trả về 0.
# + Nếu giải pháp hợp lệ:
#    => Thì trả về tổng giá trị của các item được chọn.

# evaluate a solution


def evaluate_solution(W, w, v, c, x):
    if np.sum(w * x) > W:
        return 0  # invalid solution
    val = np.sum(v * x)
    for j in range(1, c.max()+1):
        if np.sum(v[c == j] * x[c == j]) == 0:
            # invalid solution (at least one item from each class must be selected)
            return 0
    return val

 # === Tạo ra k trạng thái ban đầu ngẫu nhiên ===
 # Mỗi trạng thái là một vector n phần tử với các giá trị 0 hoặc 1.

# generate initial states (randomly)


def generate_initial_states(n, k, c):
    states = np.zeros((k, n), dtype=int)
    selected_items = set()  # set of selected item indices
    for i in range(k):
        # randomly select one item from each class
        for j in range(1, c.max()+1):
            items_in_class = np.where(c == j)[0]
            random_item = np.random.choice(items_in_class)
            selected_items.add(random_item)
            states[i][random_item] = 1
    return states

# === Tạo ra các trạng thái con ===
# Bằng cách đảo ngược một số bit trong trạng thái đầu vào.
# Tổng số trạng thái con là n*k.

# generate descendant states by flipping some bits



def generate_descendants(states, weights, capacity, n, k):
    descendants = np.zeros((k*n, n), dtype=int)
    for i in range(k):
        for j in range(n):
            descendants[i*n+j] = np.copy(states[i])
            descendants[i*n+j, j] = 1 - descendants[i*n+j, j]
            if np.dot(descendants[i*n+j], weights) > capacity:
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
    best_states = [states[i] for i in best_indices]
    return best_states


# === Thực hiện thuật toán tìm kiếm địa phương Beam Search ===
# Hàm trả về giá trị và trạng thái của giải pháp tốt nhất tìm được.

# local beam search algorithm


def local_beam_search(W, m, w, v, c, k):
    n = len(w)  # Get the size of w
    states = generate_initial_states(n, k, c)
    best_state = np.zeros(n, dtype=int)
    best_val = 0
    while True:
        descendants = generate_descendants(states, w, W, n, k)
        best_states = select_best_states(W, w, v, c, descendants, k)
        improved = False
        for i in range(k):
            val = evaluate_solution(W, w, v, c, best_states[i])
            if val > best_val:
                best_state = np.copy(best_states[i])
                best_val = val
                improved = True
        if not improved:
            break
    states = best_states
    return best_val, best_state


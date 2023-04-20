import numpy as np
import itertools

# === Calculating the value of a state ===
# If the total weight of the items is greater than the capacity of the Knapsack:
#   => Then the solution is invalid and returns 0.
# If the solution is valid:
#   => Then returns the total value of the selected items.

# evaluate a solution

def evaluate_solution(W, w, v, c, x):
    if np.sum(w * x) > W:
        return 0  # invalid solution
    val = np.sum(v * x)
    return val

# === Generate k random initial states ===
# Each state randomly selects an item from each class
# Make sure each class has at least 1 item according to the problem requirement
# The return result is a numpy matrix with:
# + k rows and n columns
# + Where n is the number of items.

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

# === Generate substates of all current states ===
# By inverting some bits in the input state.
# The total number of substates is n*k.
# This function returns a 2D numpy array

# generate descendant states by flipping some bits

def generate_descendants(states, weights, capacity, n, k):
    # set a matrix of descendant state with k*n row and n column
    descendants = np.zeros((k*n, n), dtype=int) 
    # with every parent state out of k parent states
    for i in range(k):
        # with every descendant state in parent state
        for j in range(n):
            # Copy the parent state to i*n+j descendant state
            descendants[i*n+j] = np.copy(states[i]) 
            # Invert the value of item j in the i*n+j .th descendant state
            descendants[i*n+j, j] = 1 - descendants[i*n+j, j]
            if np.dot(descendants[i*n+j], weights) > capacity:
                descendants[i*n+j, j] = 1 - descendants[i*n+j, j]
    return descendants

# === Choose the best k states from a set of states ===
# The objective function here is the value of the solution.
# To select the best state, this function uses the evaluate_solution function:
# + Calculate the value of each state
# + Sort the states in descending order of this value.
# + Finally, the function returns k best states.


# select the best k states according to the objective function

def select_best_states(W, w, v, c, states, k):
    values = np.zeros(k)
    for i in range(k):
        values[i] = evaluate_solution(W, w, v, c, states[i])
    best_indices = np.argsort(values)[::-1][:k]  # indices of k best states
    best_states = [states[i] for i in best_indices]
    return best_states


# === Implement Beam Search Local Algorithm ===
# The function returns the value and status of the best solution found.

# Start state is generated using generate_initial_states function,
# Then proceed to generate all substates by
# + Use generate_descendants function.
# Of the generated sub-states, only the best k can be extracted by
# + Use select_best_states function.
# + If the best state found by this method is better than the current best state
# => We update the current best state and optimal value.
# => This process is repeated until no further improvement is possible.
# The final result returned is the optimal value and the state corresponding to that optimal value.

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
from queue import PriorityQueue

class Node:
    # A node in the branch and bound search tree.

    def __init__(self, level, value, weight, bound, included_items):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound
        self.included_items = included_items

    def __lt__(self, other):
        return self.bound > other.bound

def bound(node, n, capacity, values, weights):
    """
        Calculate the upper bound on the maximum value that can be obtained by including items 
        in the knapsack starting from the current node.
    """
    if node.weight >= capacity:
        return 0

    value_bound = node.value
    weight_bound = node.weight
    for i in range(node.level, n):
        if weight_bound + weights[i] <= capacity:
            value_bound += values[i]
            weight_bound += weights[i]
        else:
            remaining_capacity = capacity - weight_bound
            value_bound += values[i] * (remaining_capacity / weights[i])
            break

    return value_bound

def branch_and_bound(n, capacity, values, weights):
    """
        Solve the knapsack problem using branch and bound search.
        Returns the maximum value that can be obtained by including items in the knapsack.
    """
    q = PriorityQueue()
    root = Node(-1, 0, 0, 0, [])
    q.put(root)
    max_value = 0

    while not q.empty():
        node = q.get()
        if node.bound > max_value:
            level = node.level + 1
            included_items = node.included_items.copy()
            included_items.append(level)
            bound_value = node.value + values[level]
            bound_weight = node.weight + weights[level]
            bound_bound = bound(Node(level, bound_value, bound_weight, 0, included_items), n, capacity, values, weights)
            if bound_bound > max_value:
                max_value = bound_bound
            if bound_weight <= capacity and bound_bound > max_value:
                max_value = bound_bound
            if bound_bound > max_value:
                q.put(Node(level, bound_value, bound_weight, bound_bound, included_items))

            not_included_bound = bound(Node(level, node.value, node.weight, 0, included_items), n, capacity, values, weights)
            if not_included_bound > max_value:
                q.put(Node(level, node.value, node.weight, not_included_bound, included_items))

    return max_value
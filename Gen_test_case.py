import random


class Node:
    def __init__(self, weight, value, class_type, ans=0):
        self.weight = weight
        self.value = value
        self.type = class_type
        self.ans = ans


def generate_dataset(size, num_of_class):
    arr = []
    min_weight = max_weight = 0
    for i in range(num_of_class):
        arr.append(
            Node(
                random.random() * random.randint(1, 100),
                random.randint(1, 100),
                i + 1,
                1,
            )
        )
        min_weight += arr[i].weight
    for i in range(size - num_of_class):
        arr.append(
            Node(
                random.random() * random.randint(1, 100),
                random.randint(1, 100),
                random.randint(1, num_of_class),
            )
        )
    # max_weight = sum of weight of all items
    max_weight = sum([i.weight for i in arr])
    random.shuffle(arr)
    return (
        random.randint(int(min_weight), int(max_weight)),
        num_of_class,
        arr,
    )


def print_dataset(capacity, num_of_class, dataset, filename="dataset.txt"):
    with open(filename, "w") as file:
        file.write(str(capacity) + "\n")
        file.write(str(num_of_class) + "\n")
        file.write(", ".join([str(i.weight) for i in dataset]) + "\n")
        file.write(", ".join([str(i.value) for i in dataset]) + "\n")
        file.write(", ".join([str(i.type) for i in dataset]) + "\n")
        file.write(", ".join([str(i.ans) for i in dataset]) + "\n")


def main():
    capacity, num_of_class, dataset = generate_dataset(1000, 10)
    print_dataset(capacity, num_of_class, dataset, "INPUT_" + str(capacity) + ".txt")
    #print(verify_answer("test/1500.txt", "test/output.txt"))


if __name__ == "__main__":
    main()
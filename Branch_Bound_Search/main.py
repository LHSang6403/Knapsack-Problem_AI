import ReadInput as RI
import os
import BranchBoundSearching

def main():
    current_dir = os.getcwd()
    input_file = os.path.join(current_dir, 'INPUT_1.txt')
    #print(input_file)
    n, k, arr = RI.ReadInput(input_file)

    print(BranchBoundSearching.branch_and_bound(n, arr[0], arr[1]))

main()
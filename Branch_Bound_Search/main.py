import os
import sys
import BranchBoundSearching

def main():
    current_dir = os.getcwd()
    sys.path.append(current_dir)
    input_file = os.path.join(current_dir, 'INPUT_1.txt')
    output_file = os.path.join(current_dir, 'OUTPUT_1.txt')

    BNB = BranchBoundSearching.Problem(input_file, output_file)
    BNB.SolveKnapsackUsingBNB()

main()
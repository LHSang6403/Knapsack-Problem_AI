import os

current_dir = os.getcwd()
input_file = os.path.join(current_dir, 'INPUT_1.txt')

if os.path.isfile(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        # do something with the file content
else:
    print('Error: Input file not found!')
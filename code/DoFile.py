
# Để import module này cần sử dụng lệnh này vào file main:
# import os
# import sys
# current_directory = os.getcwd()
# sys.path.append(current_directory)
# from DoFile import *

# P/s: Có thể dùng current_directory như đường dẫn dẫn đến thư mục mà không cần phải ghi lại đường dẫn

import numpy as np
import os

# Đọc dữ liệu đầu vào từ file và trả về thông tin về:
# + Trọng lượng của Knapsack
# + Số lượng loại item
# + Trọng lượng
# + Giá trị
# + Lớp của từng item.

# read input from file


def read_input(filename):
    with open(filename, 'r') as f:
        W = int(f.readline().strip())  # knapsack capacity
        m = int(f.readline().strip())  # number of classes
        # item weights
        w = np.array(list(map(float, f.readline().strip().split(','))))
        # item values
        v = np.array(list(map(int, f.readline().strip().split(','))))
        # item classes
        c = np.array(list(map(int, f.readline().strip().split(','))))
    return W, m, w, v, c


# === Ghi kết quả tìm được vào file đầu ra ===

# write output to file
def write_output(filename, opt_val, opt_sol):
    with open(filename, 'w') as f:
        f.write(str(opt_val) + '\n')
        f.write(', '.join(str(x) for x in opt_sol) + '\n')

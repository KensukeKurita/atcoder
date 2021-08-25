# coding : utf - 8
import numpy as np

def main_new():
    row, column = map(int, input().split())
    # M = np.empty((row, column), dtype=int)
    # for i in range(row):
    #     M[i, :] = [int(a) for a in input().split()]

    M = np.array([input().split() for _ in range(row)], dtype=np.int64)
    
    column_list = M.sum(axis=0)
    row_list = M.sum(axis=1)
    # for i in range(column):
    #     column_list.append(np.sum(M[:, i]))

    for i in range(row):
        for j in range(column):
            print("{} ".format(column_list[j] + row_list[i] - M[i, j]), end="")
        print("\n", end="")
    
    return 

main_new()
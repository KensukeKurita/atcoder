# coding : utf-8
import copy

def main():
    N = int(input())
    A = [int(a) for a in input().split()]

    ori_A = copy.deepcopy(A)
    A.sort()
    print(ori_A.index(A[-2])+1)

main()
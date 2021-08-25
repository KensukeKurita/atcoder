# coding: utf-8

def cal(A, N):

    B = []
    for i in range(N):
        if A[i] % 2 == 1:
            return A, False 

        B.append(A[i]/2)

    
    return B, True 

def main():

    N = int(input())
    A = [int(a) for a in input().split()]
    flag = True
    count = 0
    while flag:
        A, flag = cal(A, N) 
        if not flag:
            break
        count += 1

    print(count)

if __name__=="__main__":
    main()


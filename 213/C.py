# coding : utf-8

def main():
    H, W, N = map(int, input().split())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)


    no_A = set(range(1, H+1)) - set(A)
    no_B = set(range(1, W+1)) - set(B)
    
    for no_a in sorted(no_A, reverse=True):
        new_A = [a-1 if a > no_a else a for a in A]
        A = new_A


    for no_b in sorted(no_B, reverse=True):
        new_B = [b-1 if b > no_b else b for b in B]
        B = new_B

    for i in range(N):
        print("{} {}".format(A[i], B[i]))

    return 

main()

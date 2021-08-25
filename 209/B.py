# coding : utf-8

def main():
    N, X = map(int, input().split())
    A = [int(a) for a in input().split()]
    if N % 2 == 0:
        total = sum(A) - N//2
    else:
        total = sum(A) - (N-1)//2
    
    if X >= total:
        print("Yes")
    else:
        print("No")

main()
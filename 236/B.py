
N = int(input())
A = [int(Ai) for Ai in input().split()]

total = sum(list(range(1, N+1))) * 4
sum_A = sum(A)
print(total - sum_A)

N = int(input())
X = [int(x) for x in input().split()]

X.sort()
trim_X = X[N:4*N]
print(sum(trim_X) / float(len(trim_X)))
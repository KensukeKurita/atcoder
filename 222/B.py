
N, P = map(int, input().split())
a = [int(i) for i in input().split() if int(i) < P]
print(len(a))
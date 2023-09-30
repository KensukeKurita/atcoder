N, M = map(int, input().split())
S = input()
T = input()

if str(T).startswith(S) and str(T).endswith(S):
    print(0)
elif str(T).startswith(S):
    print(1)
elif str(T).endswith(S):
    print(2)
else:
    print(3)
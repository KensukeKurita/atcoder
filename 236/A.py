
S = input()
a, b = map(int, input().split())

a = a-1
b = b-1
print("{}".format(S[0:a] + S[b] + S[a+1:b] + S[a] + S[b+1:len(S)]))

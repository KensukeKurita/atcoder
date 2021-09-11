
P = [int(a) for a in input().split()]
alpha = "abcdefghijklmnopqrstuvwxyz"

S = ""
for i in P :
	S = S + alpha[i-1]

print(S)
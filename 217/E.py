
A = []
Q = int(input())
for i in range(Q):
	q = input()
	if q == str(2):
		print(A[0])
		# A.pop(0)
		A = A[1:len(A)]
	elif q == str(3):
		A.sort()
	else:
		q, x = map(int, q.split())
		A.append(x)


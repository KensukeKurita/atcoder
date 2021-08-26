import math

N = int(input())
if N == 1:
	print(str(0))
else:
	# n = np.log2(N)
	n = math.log2(N)
	ans = math.floor(n)
	print(ans)

import math
import sys
import numpy as np

# N = int(input())
N = 2 **50 - 1

n_f = float(N)
n_i = int(N)

if N == n_i:
	print("OK")
else:
	print("NG")

if N > sys.maxsize or N > sys.float_info.max:
	print("Over")

if N == 1:
	print(str(0))
else:
	n = np.log2(N)
	# n = 30 + math.log2(NN)
	# ans = math.floor(n)
	print(np.power(2, n))
	ans = int(n)
	print(ans)

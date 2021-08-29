"""
def check(N, list_r):
	n = 0
	for ss in list_r:
		if ss == "A":
			n += 1
		else:
			n = n * 2

	if N == n:
		print("OK {}  {}".format(N, n))
	else:
		print("NG {}  {}".format(N, n))
"""

# 最後の操作から順に考える。
# 奇数なら1引いて(A)、偶数なら2で割る(B)。
def func(n):
	if n % 2 == 0:
		return "B", int(n // 2)
	else:
		return "A", int(n - 1)

S = []
N = int(input())
# N = 10 ** 17 - 1
M = N
while M != 0:
	s, i = func(M)
	S.append(s)
	M = i

S.reverse()

result = ""
for kotae in S:
	result += kotae
print(result)
# print(len(result)) < 120

# check(N, S)

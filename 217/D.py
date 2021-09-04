import bisect

def time_over():

	L, Q = map(int, input().split())
	cut_point = [0, L]
	list_check = []
	for i in range(Q):
		c, x = map(int, input().split())
		if c == 1:
			cut_point.append(x)
		else:
			cut_point.append(x)
			cut_point.sort()
			n = cut_point.index(x)
			print(cut_point[n+1] - cut_point[n-1])
			cut_point.remove(x)


def binary_search_find_closest(data, target):

	min_diff = float('inf')
	imin = 0
	imax = len(data) - 1
	while imin <= imax:
		imid = imin + (imax - imin) // 2
		# 　中心の左右の値と目標との差を計算する。
		if imid + 1 < len(data):
			min_diff_right = abs(data[imid + 1] - target)
		if imid >= 0:
			min_diff_left = abs(data[imid - 1] - target)
		# 最初の差と最も最小に近い値を更新する。
		if min_diff_left < min_diff:
			min_diff = min_diff_left
			res = imid - 1
		if min_diff_right < min_diff:
			min_diff = min_diff_right
			res = imid + 1
		# 2分探索する。
		if data[imid] < target:
			imin = imid + 1
		elif data[imid] > target:
			imax = imid - 1
		else:
			return data[imid]

	if target < data[res]:
		res = res - 1

	return res


def now():

	L, Q = map(int, input().split())
	cut_point = [0, L]
	for i in range(Q):
		c, x = map(int, input().split())
		if c == 1:
			bisect.insort_left(cut_point, x)
		else:
			# n = binary_search_find_closest(cut_point, x)
			n = bisect.bisect_left(cut_point, x) - 1
			print(cut_point[n+1] - cut_point[n])

now()
# time_over()
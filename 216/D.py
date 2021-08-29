import collections


def get_last(A):

	list_last = []
	for aa in A:
		list_last.append(aa[-1])
	return list_last


N, M = map(int, input().split())

k = []
a = []
for i in range(M):
	k.append(int(input()))
	a.append([int(x) for x in input().split()])

isOK = True
for time in range(N):
	l = get_last(a)

	# 重複している色を検出
	ll = [k for k, v in collections.Counter(l).items() if v > 1]

	# 重複している色が無ければ、break
	if len(ll) == 0:
		isOK = False
		break

	# 重複している色の位置を検出
	ok_list = [i for i, j in enumerate(l) if j == ll[0]]
	for p in ok_list:
		a[p].pop(-1)

if isOK:
	print("Yes")
else:
	print("No")

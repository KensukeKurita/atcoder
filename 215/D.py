import math
N, M = map(int, input().split())
A = [int(a) for a in input().split()]
A.sort()
A = set(A)


def slow():
	result = []
	for i in range(1, M+1):
		flag = True
		for a in A:
			gcd = math.gcd(a, i)
			if gcd != 1:
				flag = False
				break
		if flag:
			result.append(i)

	return result


def fast():
	result = []
	remove_list = set()
	for i in range(1, M+1):
		flag = True

		if i in remove_list:
			continue

		for a in A:
			gcd = math.gcd(a, i)
			if gcd != 1:
				flag = False
				break
		if flag:
			result.append(i)
		else:
			remove_list = remove_list | set(i*j for j in range(int(M/i)))

	return result


kotae = fast()
print(len(kotae))
for i in kotae:
	print(i)
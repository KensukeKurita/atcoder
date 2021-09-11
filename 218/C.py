import numpy as np


def rotation(A):
	"""
	counter clock wise rotation.
	"""

	AA = np.empty((N, N), dtype="str")
	for i in list(range(N)).__reversed__():
		AA[:, i] = A[i, :]

	return AA


def move(A):

	gyou = -1
	for i in range(N):
		if "#" in A[i, :]:
			gyou = i
			break

	retu = -1
	for i in range(N):
		if "#" in A[:, i]:
			retu = i
			break

	AA = np.delete(A, list(range(gyou)), 0)
	empty = np.full((gyou, N), ".")
	AA = np.append(AA, empty, axis=0)

	empty = np.full((N, retu), ".")
	AA = np.delete(AA, list(range(retu)), 1)
	AA = np.append(AA, empty, axis=1)

	"""
	shape = AAA.shape
	gyou = []
	for ii in range(shape[0]):
		if not "#" in AAA[ii, :]:
			gyou.append(ii)
	retu = []
	for ii in range(shape[1]):
		if not "#" in AAA[:, ii]:
			retu.append(ii)

	if len(gyou) != 0:
		AAA = np.delete(AAA, gyou, 0)
	if len(retu) != 0:
		AAA = np.delete(AAA, retu, 1)
	"""

	return AA


def main():

	TT = move(T)

	S0_move = move(S)

	S1 = rotation(S)
	S1_move = move(S1)

	S2 = rotation(S1)
	S2_move = move(S2)

	S3 = rotation(S2)
	S3_move = move(S3)

	for i in range(N):
		print(*TT[i])
	print("")
	for i in range(N):
		print(*S0_move[i])
	print("")
	for i in range(N):
		print(*S1_move[i])
	print("")
	for i in range(N):
		print(*S2_move[i])

	print("")
	for i in range(N):
		print(*S3_move[i])

	if np.all(TT == S1_move):
		print("Yes")
		return
	elif np.all(TT == move(rotation(S1))):
		print("Yes")
		return
	elif np.all(TT == move(rotation(rotation(S1)))):
		print("Yes")
		return
	else:
		print("No")


if __name__ == "__main__":
	N = int(input())
	S = []
	for i in range(N):
		S.append([a for a in input()])
	S = np.array(S)

	T = []
	for i in range(N):
		T.append([a for a in input()])
	T = np.array(T)

	# empty[0, :] = np.array(["." for i in range(N)])

	main()

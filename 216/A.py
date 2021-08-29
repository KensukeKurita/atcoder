# coding : utf-8

a = float(input())
X = int(a)
Y = int((a - int(a)) * 10) # ここ？

if 0 <= Y <= 2:
	print("{}-".format(X))
elif 3 <= Y <= 6:
	print("{}".format(X))
elif 7 <= Y <= 9:   # ここ？
	print("{}+".format(X))
else:
	pass

# coding : utf-8

N = int(input())
list_name = []
for i in range(N):
	s, t = input().split()
	list_name.append("{}-{}".format(s, t))

set_name = set(list_name)

if len(list_name) > len(set_name):
	print("Yes")
else:
	print("No")

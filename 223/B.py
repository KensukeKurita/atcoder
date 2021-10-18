# coding : utf-8

def right_shift(s):
    return s[1:len(s)] + s[0]

S = input()

list_s = []
next_s = S
for i in range(len(S)):
    next_s = right_shift(next_s)
    list_s.append(next_s)
tuple = set(list_s)
list_s = list(tuple)
list_s.sort()
print(list_s[0])
print(list_s[-1])

import string

S = input()
for i, s in enumerate(S):
    if s.isupper():
        print(i + 1)
    else:
        pass

n = input()
S = input()
if "ABC" not in S:
    print(-1)
else:
    print(S.find("ABC") + 1)
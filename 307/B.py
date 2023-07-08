import itertools

def isRotate(S):
    if len(S) % 2 == 0:
        s1 = S[0:len(S)//2]
        s2 = S[len(S)//2::]
        s2 = s2[::-1]
        if s1 == s2:
            return True
        else:
            return False
    else:
        s1 = S[0:(len(S)-1)//2]
        s2 = S[(len(S)-1)//2+1::]
        s2 = s2[::-1]
        if s1 == s2:
            return True
        else:
            return False

N = int(input())
list_S = []
for _ in range(N):
    list_S.append(input())

for x, y in itertools.permutations(list_S, 2):
    if isRotate(x+y):
        print("Yes")
        break
    else:
        continue
else:
    print("No")
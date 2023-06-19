N = int(input())
A = [int(a) for a in input().split()]

Ai = A[0]
for Aip in A[1::]:
    if abs(Aip - Ai) == 1:
        print(str(Ai), end=" ")
    elif Ai < Aip:
        tmp = [str(a) for a in range(Ai+1, Aip)]
        print(str(Ai) + " " + " ".join(tmp), end=" ")
    else:
        tmp = [str(a) for a in range(Ai-1, Aip, -1)]
        print(str(Ai) + " " +  " ".join(tmp), end=" ")
    Ai = Aip
print(Aip)
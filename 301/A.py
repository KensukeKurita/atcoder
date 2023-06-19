N = int(input())
if N % 2 == 0:
    kachisu = N / 2 
else:
    kachisu = N // 2 +1


Str = input()
T = 0
A = 0
for s in Str:
    if s == "T":
        T += 1
    else:
        A +=1
    
    if T >= kachisu:
        print("T")
        break

    if A >= kachisu:
        print("A")
        break

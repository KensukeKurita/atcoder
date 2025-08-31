
def check() :
    count = 0
    for x in L :
        if x >= T:
            count += 1
            
    if count >= P :
        return True
    else:
        return False

    
N, T, P = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]


day = 0
while True:
    if check() :
        print(day)
        break
    else:
        for i in range(len(L)):
            L[i] += 1
        day += 1
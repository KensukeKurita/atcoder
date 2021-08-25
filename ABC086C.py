# coding : utf-8
def check(now_x, now_y, next_x, next_y, time):

    dx = next_x - now_x
    dy = next_y - now_y

    d = abs(dx) + abs(dy)
    if d > time:
        return False
        
    if (time - d) % 2 == 0:
        return True
    else:
        return False


def main():

    N = int(input())
    T, X, Y = [0], [0], [0]
    for i in range(N):
        t, x, y = map(int, input().split())
        T.append(t)
        X.append(x)
        Y.append(y)

    for i in range(N):
        if not check(X[i], Y[i], X[i+1], Y[i+1], T[i+1]-T[i]):
            print("No")
            return 

    print("Yes")
    return 
            

if __name__=="__main__":
    main()

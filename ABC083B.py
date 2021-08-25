# coding : utf-8
def wa(num):

    a4 = int(num/(10**4))
    a3 = int( (num-a4*10**4)/(10**3) )
    a2 = int( (num-a4*10**4-a3*10**3)/(10**2) )
    a1 = int( (num-a4*10**4-a3*10**3-a2*10**2)/(10**1) )
    a0 = int( (num-a4*10**4-a3*10**3-a2*10**2-a1*10**1) )

    return a4 + a3 + a2 + a1 + a0

def main():

    N, A, B = map(int, input().split())
    count = 0
    for i in range(1, N+1):
        w = wa(i)
        if w >= A and w <= B:
            count += i

    print(count)

if __name__=="__main__":
    main()

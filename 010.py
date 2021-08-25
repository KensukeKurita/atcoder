# coding : utf-8

def main():
    N = int(input())
    one = [0]
    two = [0]
    for i in range(N):
        a, b = map(int, input().split())
        if a == 1:
            one.append(one[i]+b)
            two.append(two[i]+0)
        else:
            one.append(one[i]+0)
            two.append(two[i]+b)
    
    Q = int(input())
    for i in range(Q):
        l, r = map(int, input().split())
        print("{} {}".format(one[r]-one[l-1], two[r]-two[l-1]))
    #   1 2 3
    #   2 3 5
    # 0 2 5 10 
    # 

main()

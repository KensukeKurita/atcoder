# coding : utf-8
# t=1 [1 2 3 5]
# t=2 [4 6 7 8]
# up 5 3 2 1 / 4 6 7 8
# if x=6, 6(t2[6-len(t1)])

def new():
    Q = int(input())
    data = [[], []]
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 3:
            if x <= len(data[0]):
                # [-3, -2, -1]
                print(data[0][-x])
            else:
                print(data[1][x - len(data[0]) - 1])

        else:
            data[t-1].append(x)


def main():
    Q = int(input())
    yama = []
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            yama = [x] + yama
        elif t == 2:
            yama.append(x) 
        else:
            print(yama[x-1])
    
    return 

# main()
new()
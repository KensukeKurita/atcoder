# coding : utf-8

# x + y + z = N
# x = 0, N
#   y = 0, N - x
#       z = N - x -y

def main():
    N, Y = map(int, input().split())

    for x in range(0, N+1):
        for y in range(0, N-x+1):
            z = N - x - y
            sum_num = x * 10000 + y * 5000 + z * 1000
            if sum_num == Y:
                print("{} {} {}".format(x, y, z))
                return 

    print("-1 -1 -1")
    return 


if __name__=="__main__":
    main()

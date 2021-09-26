
A, B, C = map(int, input().split())

def main():
    for i in range(1000):
        c = C * i
        if (c >= A) and (c <= B):
            print(c)
            return

    print(-1)
    return

main()
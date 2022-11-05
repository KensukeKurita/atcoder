# coding : utf-9

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    A = list(set(A))

    i = 0
    for a in A:
        if i != a:
            print(i)
            return
        i += 1

    print(i)
    return


if __name__ == "__main__":
    main()
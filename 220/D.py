import array


def main():
    D = 998244353
    N = int(input())
    A = [int(a) for a in input().split()]
    arr = array.array("i", A)
    print(arr)

main()
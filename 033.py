def main():
    H, W = map(int, input().split())
    if H == 1 or W == 1:
        print(H*W)
    else:
        a = (H+1)//2
        b = (W+1)//2
        print(a*b)

main()
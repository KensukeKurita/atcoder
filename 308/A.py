

def main():
    S = [int(x) for x in input().split()]
    if S[0] % 25 != 0:
        print("No")
        return

    if S[0] >= 100 and S[0] <= 675:
        pass
    else:
        print("No")
        return

    for i in range(1, len(S)):
        if S[i] % 25 != 0:
            print("No")
            return

        if S[i] >= 100 and S[i] <= 675:
            pass
        else:
            print("No")
            return

        if S[i-1] > S[i]:
            print("No")
            return
    else:
        print("Yes")

main()

def main():
    S = input()
    N = int(input())

    max_num = int(S.replace("?", "1"), 2)
    min_num = int(S.replace("?", "0"), 2)

    if N >= max_num:
        print(max_num)
        return
    if N < min_num:
        print(-1)
        return


    N2 = bin(N).replace("0b","")
    if len(S) >= len(N2):
        N2 = "0" * (len(S) - len(N2)) + N2
    else:
        RuntimeError("Error")

    flag = True
    for i in range(len(S)):
        if N2[i] == "1":
            flag = False
        if flag and S[i] == "?":
            S = S[:i] + "0" + S[i+1:]

        if (not flag) and (S[i] == "?"):
            S = S[:i] + "1" + S[i+1:]
            flag = True

    print(int(S, 2))

if __name__ == "__main__":
    main()
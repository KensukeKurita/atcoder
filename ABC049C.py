# coding : utf-8

def removeprefix(s, prefix):
    if s.endswith(prefix):
        return s[:-len(prefix)]
    else:
        return s

def main():
    S = input()

    flag = True
    while len(S) != 0:
        if S[-7:] == "dreamer":
            S = removeprefix(S, "dreamer")
        elif S[-6:] == "eraser":
            S = removeprefix(S, "eraser")
        elif S[-5:] == "dream":
            S = removeprefix(S, "dream")
        elif S[-5:] == "erase":
            S = removeprefix(S, "erase")
        else:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")

if __name__=="__main__":
    main()

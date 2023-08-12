
def main():

    N = int(input())
    S = str(input())
    Q = int(input())

    Change_list = {} # x文字目が変わったときは、最終変更の情報だけ持っておけばいい。
    Upper_timing = []
    Lower_timing = []
    last_operator = ""
    for i in range(Q):
        line = input()
        if line[0] == str(1):
            x, c = line[1::].split()
            Change_list[str(int(x)-1)] = (i, c)
        elif line[0] == str(2):
            Lower_timing.append(i)
            last_operator = "Lower"
        else:
            Upper_timing.append(i)
            last_operator = "Upper"

    if last_operator == "":
        # 何もしないとき
        for i in range(len(S)):
            if str(i) in Change_list.keys():
                print(Change_list[str(i)][1], end="")
            else:
                print(S[i], end="")
        return

    for i in range(len(S)):
        if str(i) in Change_list.keys():
            timing = Change_list[str(i)][0]
            if timing > Lower_timing[-1] and timing > Upper_timing[-1]:
                print(Change_list[str(i)][1], end="")
            elif timing < Lower_timing[-1] and timing < Upper_timing[-1]:
                if last_operator == "":
                    print(Change_list[str(i)][1], end="")
                elif last_operator == "Lower":
                    print(Change_list[str(i)][1].lower(), end="")
                else:
                    print(Change_list[str(i)][1].upper(), end="")
            elif timing > Lower_timing[-1] and timing < Upper_timing[-1]:
                print(Change_list[str(i)][1].upper(), end="")
            else:        # この文字の変更後に文字列の操作がある場合
                print(Change_list[str(i)][1].lower(), end="")

        else:
            if last_operator == "":
                print(S[i], end="")
            elif last_operator == "Lower":
                print(S[i].lower(), end="")
            else:
                print(S[i].upper(), end="")

    return

if __name__=="__main__":
    main()
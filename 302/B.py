
def main():
    H, W = map(int, input().split()) 

    find_str = "snuke"
    find_str_reverse = "ekuns"

    # 縦、よこ、ななめ、の文字列を作成してしまう。
    list_yoko = []
    list_tate = []

    # 横
    for i in range(H):
        S = input()
        list_yoko.append(S)

        # 判定
        position = S.find(find_str)
        if position != -1:
            for C in range(5):
                print(i+1, position+1 + C)
            return
        # 逆順判定
        position = S.find(find_str_reverse)
        if position != -1:
            for C in range(5):
                print(i+1, position+1+4 - C)
            return

    # 縦
    for j in range(W):
        T = ""
        for i in range(H):
            T += list_yoko[i][j]
        list_tate.append(T)

    for j in range(W):
        T = list_tate[j]
        # 判定
        position = T.find(find_str)
        if position != -1:
            for R in range(5):
                print(position+1 + R, j+1)
            return
        # 逆順判定
        position = T.find(find_str_reverse)
        if position != -1:
            for R in range(5):
                print(position+1+4 - R, j+1)

    # ななめ
    for i in range(H-4):
        for j in range(W):
            # (i, j)を支点に5文字作る
            # 右下方向 i++, j++
            if j <= W-1-4:
                S = list_yoko[i][j] + list_yoko[i+1][j+1] + list_yoko[i+2][j+2] + list_yoko[i+3][j+3] + list_yoko[i+4][j+4]
            # 判定
            position = S.find(find_str)
            if position != -1:
                for R in range(5):
                    print(i+1 + R, j+1 + R)
                return
            # 逆順判定
            position = S.find(find_str_reverse)
            if position != -1:
                for R in range(5):
                    print(i+1+4 - R, j+1+4 - R)
                return

            # 左下方向 i++, j--
            if j >= 4:
                S = list_yoko[i][j] + list_yoko[i+1][j-1] + list_yoko[i+2][j-2] + list_yoko[i+3][j-3] + list_yoko[i+4][j-4]
            # 判定
            position = S.find(find_str)
            if position != -1:
                for R in range(5):
                    print(i+1 + R, j+1 - R)
                return
            # 逆順判定
            position = S.find(find_str_reverse)
            if position != -1:
                for R in range(5):
                    print(i+1+4 - R, j+1+4 +R)
                return



if __name__ == "__main__":
    main()
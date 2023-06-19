
def main():
    H, W = map(int, input().split()) 

    find_str = "snuke"
    find_str_reverse = "ekuns"

    # 横
    list_yoko = []
    for i in range(H):
        S = input()
        list_yoko.append(S)

    for R in range(H):
        for C in range(W):
            # 横の判定 R, C++
            if C <= W-1-4:
                S = list_yoko[R][C] + list_yoko[R][C+1] + list_yoko[R][C+2] + list_yoko[R][C+3] + list_yoko[R][C+4]
                if S == find_str:
                    for i in range(5):
                        print(R+1, C+1 + i)
                    return
                if S == find_str_reverse:
                    for i in range(5):
                        print(R+1, C+1+4 - i)
                    return
            
            # 縦の判定 R++, C
            if R <= H-1-4:
                S =  list_yoko[R][C] + list_yoko[R+1][C] + list_yoko[R+2][C] + list_yoko[R+3][C] + list_yoko[R+4][C]
                if S == find_str:
                    for i in range(5):
                        print(R+1 + i, C+1)
                    return
                if S == find_str_reverse:
                    for i in range(5):
                        print(R+1+4 - i, C+1)
                    return

            # ななめの判定
            # 右下方向 R++, C++
            if C <= W-1-4 and R <= H-1-4:
                S = list_yoko[R][C] + list_yoko[R+1][C+1] + list_yoko[R+2][C+2] + list_yoko[R+3][C+3] + list_yoko[R+4][C+4]
                if S == find_str:
                    for i in range(5):
                        print(R+1 + i, C+1 + i)
                    return
                # 逆順判定
                if S == find_str_reverse:
                    for i in range(5):
                        print(R+1+4 - i, C+1+4 - i)
                    return

            # 左下方向 R++, C--
            if C <= 4 and R <= H-1-4:
                S = list_yoko[R][C] + list_yoko[R+1][C-1] + list_yoko[R+2][C-2] + list_yoko[R+3][C-3] + list_yoko[R+4][C-4]
                if S == find_str:
                    for i in range(5):
                        print(R+1 + i, C+1 - i)
                    return
                if S == find_str_reverse:
                    for i in range(5):
                        print(R+1-4 + i, C+1+4 - i)
                    return


if __name__ == "__main__":
    main()
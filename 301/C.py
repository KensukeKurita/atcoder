import string
def main():
    atcoder = {"a", "t", "c", "o", "d", "e", "r"}

    S = input()
    T = input()

    s_dict = {}
    t_dict = {}
    s_dict["@"] = S.count("@")
    t_dict["@"] = T.count("@")
    for alpha in string.ascii_lowercase:
        s_dict[alpha] = S.count(alpha)
        t_dict[alpha] = T.count(alpha)

    # a t c o d e r 以外の文字は必ず同じ数。
    for alpha in string.ascii_lowercase:
        if alpha in atcoder:
            continue
        if s_dict[alpha] != t_dict[alpha]:
            print("No")
            return
        
    # a t c o d e r の数の差が@の数の差と等しいならOK
    diff = 0
    for at in atcoder:
        if s_dict[at] > t_dict[at]:
            t_dict["@"] = t_dict["@"] - (s_dict[at] - t_dict[at])
        elif s_dict[at] < t_dict[at]:
            s_dict["@"] = s_dict["@"] - (t_dict[at] - s_dict[at])
        else:
            pass

        if s_dict["@"] < 0 or t_dict["@"] < 0:
            print("No")
            return
        
    print("Yes")



if __name__ == "__main__":
    main()

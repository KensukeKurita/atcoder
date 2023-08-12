# coding : utf-8


def div_two_three(x: int):

    i_two = 0
    p = x % 2
    while (p == 0):
        i_two += 1
        x = x // 2
        p = x % 2

    i_three = 0
    p = x % 3
    while (p == 0):
        i_three += 1
        x = x // 3
        p = x % 3

    return i_two, i_three, x


def main():
    N = int(input())
    two, three, amari = [], [], set()
    for a in input().split():
        x1, x2, x3 = div_two_three(int(a))
        if len(amari) == 0:
            amari.add(x3)
        elif x3 not in amari:
            print(-1)
            return
        else:
            pass

        two.append(x1)
        three.append(x2)

    min_two = min(two)
    min_three = min(three)
    print(sum(two) - N * min_two + sum(three) - N * min_three)
    return


if __name__ == "__main__":
    main()

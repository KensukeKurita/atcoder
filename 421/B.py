
def f(a):
    a_str = str(a)
    rev_a_str = a_str[::-1]
    # 先頭の0を削除
    rev_a_str = rev_a_str.lstrip("0")

    return int(rev_a_str)


X, Y = map(int, input().split())
a_before = X
a_after = Y
for i in range(1, 9):
    tmp = f(a_before + a_after)
    a_before = a_after
    a_after = tmp

print(tmp)

def main():
    A, B = map(int, input().split())

    a = (bin(A))[2:]
    b = (bin(B))[2:]
    if len(a) > len(b):
        b = "0"*(len(a)-len(b)) + b
    else:
        a = "0"*(len(b)-len(a)) + a

    c = ""
    for i in range(len(a)):
        if a[i] == "1" and b[i] == "0":
            c = c + "1"
        elif a[i] == "0" and b[i] == "1":
            c = c + "1"
        else:
            c = c + "0"

    print(int(c, 2))
    return

main()
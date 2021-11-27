
def main():

    A, B = [a for a in input().split()]

    if len(A) == len(B):
        pass
    elif len(A) > len(B):
        B = "0"*(len(A) - len(B)) + B
    else:
        A = "0"*(len(B) - len(A)) + A

    for i in range(len(A)):
        a = int(A[i])
        b = int(B[i])
        if a + b >= 10:
            print("Hard")
            return

    print("Easy")
    return


if __name__ == "__main__":
    main()

# coding : utf-8

def main():

    X = input()
    a, b = X.split(".")
    if int(b[0]) >= 5:
        print(int(a)+1)
    else:
        print(int(a))

    return


if __name__ == "__main__":
    main()

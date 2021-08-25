# coding : utf-8

def main():
    A, B = map(int, input().split())
    if A > B :
        print("0")
    else:
        print("{}".format(B-A+1))

main()
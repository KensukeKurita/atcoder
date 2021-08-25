# coding : utf-8
def main():
    N = int(input())
    S = str(input())

    j = 0
    for i, s in enumerate(S):
        if s == str(1):
            j = i
            break
    
    if (j + 1) % 2 == 0:
        print("Aoki")
    else:
        print("Takahashi")

    
main()
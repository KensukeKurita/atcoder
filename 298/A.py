N = int(input())
S = input()

def main():

    if "x" in S:
        print("No")
        return
    
    if "o" in S:
        print("Yes")
        return
    else:
        print("No")
        return

if __name__=="__main__":
    main()
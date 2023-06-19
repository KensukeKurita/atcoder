
def rotate(input_matrix: list, N: int) -> list:

    output_matrix = []
    for x in input_matrix:
        output_matrix.append((N+1-x[1], x[0]))
    return output_matrix

def check(A, B) -> bool:

    for a in A:
        if a not in B:
            return False
    else:
        return True    
    
def main():
    
    N = int(input())

    A = []
    for i in range(N):
        for j, b in enumerate(input().split()):
            if b == "1":
                A.append((i+1, j+1))


    B = []
    for i in range(N):
        for j, b in enumerate(input().split()):
            if b == "1":
                B.append((i+1, j+1))

    A1 = rotate(A, N)
    if check(A1, B):
        print("Yes")
        return
    
    A2 = rotate(A1, N)
    if check(A2, B):
        print("Yes")
        return
    
    A3 = rotate(A2, N)
    if check(A3, B):
        print("Yes")
        return
    
    A4 = rotate(A3, N)  # なぜA3までだとダメ？
    if check(A4, B):
        print("Yes")
        return

    print("No")

if __name__ == "__main__":
    main()
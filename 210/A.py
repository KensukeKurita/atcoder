# codding : utf-8

def main():
    N, A, X, Y = map(int, input().split())
    
    if N >= A+1:
        total = A*X + (N-A)*Y
    else:
        total = N*X
    print(total)

main()

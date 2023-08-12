N = int(input())

A = {}
for i in range(N):
    C = int(input())
    A[str(i)] = [int(x) for x in input().split()]
X = int(input())

pay = []
min_pay = 38
for i in range(N):
    if X in A[str(i)]:
        if len(A[str(i)]) < min_pay:
            pay = []
            pay.append((str(i+1), len(A[str(i)])))
            min_pay = len(A[str(i)])
        elif len(A[str(i)]) == min_pay:
            pay.append((str(i+1), len(A[str(i)])))
    

print(len(pay))
if len(pay) == 0:
    print()    
else:
    for a, b in pay:
        print(a, end=" ")
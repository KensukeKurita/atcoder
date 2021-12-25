
import itertools

N, X = map(int, input().split())

# first
aux = list(map(int, input().split()))
r = aux[1::]


for i in range(N-1):
    aux = list(map(int, input().split()))
    aux = aux[1::]

    rr = [x*y for x, y in itertools.product(r, aux) if x*y <= X]
    r = rr

result = [x for x in r if x == X]
print(len(result))

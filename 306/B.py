A = [int(a) for a in input().split()]

kotae = 0
i = 0
for a in A:
    kotae += a * 2**i
    i += 1
print(kotae)
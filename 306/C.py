N = int(input())
A = [int(a) for a in input().split()]

first_set = set()
end_set = set()
result = ""

for a in A:
    if a not in first_set:
        first_set.add(a)
    elif a in end_set:
        continue
    else:
        result += str(a) + " "
        end_set.add(a)
print(result)
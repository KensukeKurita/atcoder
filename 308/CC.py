import bisect

N = int(input())

sorted_data = []

for i in range(N):
    A, B = map(int, input().split())
    success_rate = float(A) /  float(A + B)
    if len(sorted_data) == 0:
        sorted_data.append((i+1, success_rate))
        continue

    # 2分探索で入れていく
    left = 0
    right = i
    while left < right:
        mid = (left + right) // 2
        if sorted_data[mid][1] == success_rate:
            left = mid + 1
        elif sorted_data[mid][1] > success_rate:
            left = mid + 1
        else:
            right = mid

    sorted_data.insert(left, (i+1, success_rate))

for i in range(N):
    print(sorted_data[i][0], end=" ")

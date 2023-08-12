def approximate_value(n):
    if n <= 10**3 - 1:
        return n
    elif n <= 10**4 - 1:
        return n - (n % 10)
    elif n <= 10**5 - 1:
        return n - (n % 100)
    elif n <= 10**6 - 1:
        return n - (n % 1000)
    elif n <= 10**7 - 1:
        return n - (n % 10000)
    elif n <= 10**8 - 1:
        return n - (n % 100000)
    elif n <= 10**9 - 1:
        return n - (n % 1000000)
    else:
        return "no"

# テスト
n = int(input())
result = approximate_value(n)
print(result)
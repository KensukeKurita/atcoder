
S = {}
S["1"] = input()
S["2"] = input()
S["3"] = input()
T = input()

result = ""
for i in T:
    result += S[str(i)]

print(result)
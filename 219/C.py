

def name_decode(name, X, alpha_d):

    new_name = ""
    for s in name:
        new_name += X[alpha_d[s]-1]
    return new_name


def name_encode(new_name, X_d, alpha):
    old_name = ""
    for s in new_name:
        old_name += alpha[X_d[s]-1]
    return old_name

alpha_d = {}
alpha = "abcdefghijklmnopqrstuvwxyz"
for s in range(26):
    alpha_d[alpha[s]] = s + 1


X = input()
X_d = {}
for s in range(26):
    X_d[X[s]] = s + 1

N = int(input())
name_list = []
for i in range(N):
    name_list.append(name_decode(input(), X, alpha_d))

name_list.sort()

for nn in name_list:
    print(name_encode(nn, X_d, alpha))


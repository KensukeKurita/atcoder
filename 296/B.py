
ii = -1
SS = ""
for i in range(8):
    S = input()
    if "*" in S:
        SS = S
        ii = i

retu = "abcdefgh"
gyou = "87654321"
print(retu[SS.find("*")] + gyou[ii])
# coding : utf-8

def main():
    P = input()
    a = int(P[0])
    b = int(P[1]) 
    c = int(P[2])
    d = int(P[3]) 
    p = [a, b, c, d]
    

    num_list = list(range(0, 10))

    if len(list(set(p))) == 1:
        print("Weak")
        return 

    np = ["a"]
    for i in range(4):
        if p[i] == 9:
            x = 0
        else:
            x = p[i] + 1
        np.append(x)

    if p[1] == np[1] and p[2] == np[2] and p[3] == np[3]:
        print("Weak")
        return

    print("Strong")

main()
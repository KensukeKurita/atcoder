# coding : utf-8

def main():

    N = int(input())
    L = []
    A = []
    for i in range(N):
        flag = False
        aux = [int(a) for a in input().split()]
        l = aux[0]
        a = aux[1:len(aux)]

        for aa in A:

            if a == aa:
                flag = True
                break

        if flag == False:
            L.append(l)
            A.append(a)

    print(len(L))

    return

def main2():
    N = int(input())
    L = []
    A = set()
    for i in range(N):
        flag = False
        aux = [int(a) for a in input().split()]
        l = aux[0]
        a = tuple(aux[1:len(aux)])
        A.add(a)


    print(len(A))



if __name__ == "__main__":
    main2()

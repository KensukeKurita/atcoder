
def get_next(num):
    if num == 9:
        return 0
    else:
        return num + 1

def isOK(n):

    if get_next(int(n[0])) == int(n[1]) and get_next(int(n[1])) == int(n[2]) and get_next(int(n[2])) == int(n[3]):
        return True
    else:
         return False

    
weak = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = input()

if n[0] == n[1] == n[2] == n[3]:
    print("Weak")
elif isOK(n):
    print("Weak")
else:
    print("Strong")
    

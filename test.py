import time
l = 100000


s = time.time()
a = [0]*l
for i in range(l):
    a[i] = i*i
print(time.time()-s)


s = time.time()
b = []
for i in range(l):
    b.append(i*i)
print(time.time()-s)
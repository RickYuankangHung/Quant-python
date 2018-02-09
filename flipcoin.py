import random
c = 0
a=0
b=0
for i in range(1000000):
    r=1
    k=0
    while(random.randint(1, 4)!=4):
        r=r+1
    k=r%2
    if (k==1):
        a=a+1
    if (k==0):
        b=b+1
    if (r==4):
        c=c+1
print(a)
print(b)
print(c)

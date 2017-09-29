total=0
for n in range(2,999999):
    sum=0
    ls=[int(c) for c in str(n)]
    for index in range(0,len(ls)):
        sum+=int(ls[index])**5
    if sum==n:
        print(n)
        total+=sum
print(total)


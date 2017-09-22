def factorial(n):
    result=1
    while n>1:
        result *=n
        n-=1
    return result
print(factorial(100))
s=str(factorial(100))
sum=0
for c in s:
    sum+=int(c)
print(sum)
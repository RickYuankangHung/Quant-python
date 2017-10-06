def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    p=3
    while p*p<=n:
        if n%p==0:
            return False
        p+=2
    return True

def is_decomposited(n):
    indicator=0
    for i in range(1,int((n**(0.5)))) :
        k=n
        k=k-i*i*2
        if (is_prime(k)):
            indicator=1
    return indicator
def find(k):
    for n in range(9,k):
        if (is_prime(n))==False:
            if n%2==1:
                if is_decomposited(n)==0:
                    return n
print(find(10000000))
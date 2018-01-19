import math
def gen_prime(n):
    list_num = []
    for i in range(2, n):
        for num in range(2, int((n**0.5))+1):
            if i % num == 0 and i != num:
                break
            elif i % num != 0 and num == (int(n**0.5)):
                list_num.append(i)
    return list_num
# print(is_prime(60000))
# for i in range(21,23):
#     for j in range(len(is_prime(100))-i):
#         sum((is_prime(100)[j:j+i])


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p*p <= n:
        if n % p == 0:
            return False
        p += 2
    return True
record=21
lst=gen_prime(60000)
for i in range(21,1000):
    for j in range(len(lst)-i):
        a=lst[j:j+i]
        if is_prime(sum(a)) and sum(a)<1000000:
            print(sum(a))
            record=i
print(record)
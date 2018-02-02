from decimal import *
import math
getcontext().prec=110
sum_=0
for n in range(2,101):
    num_string=str(Decimal(n).sqrt())
    sum_ += int(num_string[0])+sum(int(c) for c in num_string[2:101])
print(sum_-sum(k for k in range(10)))
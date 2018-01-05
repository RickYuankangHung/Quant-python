### Let M~N(0,1) be market variable
### Let Ri=alpha*M+beta*Z for i=1,2,...,n where Zi~N(0,1), i.i.d.
### Find alpha,beta,
### Ri~N(0,1) and roh i,j=roh
import random
from matplotlib import pyplot as plt
import numpy
n=10
rho=0.5
num_sims=1000
beta=rho**0.5
alpha=(1-rho)**0.5

# run simulation

histogram=[0]*(n+1)

for _ in range(num_sims):
    M=random.gauss(0,1)
    count=0
    for _ in range(n):
        R_i=beta*M + alpha*random.gauss(0,1)
        if R_i>0:
            count=count+1
    histogram[count]=histogram[count]+1

print(histogram)

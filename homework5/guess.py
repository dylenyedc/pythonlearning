import math
num=int(input())
MAXNUM=2000000000
def isprime(a):
    if a<=1:
        return False
    elif a==2:
        return True
    else:
        for i in range(2,int(math.sqrt(a)+1)):
            if a%i==0:
                return False
        return True
p=2
q=num-p
while not isprime(q):
    p+=1
    while not isprime(p):
        p+=1
    q=num-p
print(num,"=",p,"+",q)
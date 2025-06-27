def powers(x,n) :
    return x**n

def fac(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return n*fac(n-1)
def sum(x):
    i=0
    s=0
    while (powers(x,i)/fac(i))>=1e-6:
        s=s+powers(x,i)/fac(i)
        i=i+1
    return s

x=int(input())
ex=sum(x)
print("%d powers of e = %.4f"%(x,ex))
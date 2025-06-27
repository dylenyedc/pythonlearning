def f1(x):
    return 1+x

def f2(x):
    return 1/(1+4*x**2)
    
def connect(f,a,b,n):
    h=(b-a)/n
    area=0    
    area=(f(a)+f(b))/2.0
    for i in range(1,n):
        area+=f(a+i*h)
    return area*h

print("%.2f" % connect(f1,0,2,100))
print("%.2f" % connect(f2,-1,1,100))
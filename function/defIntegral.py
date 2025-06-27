#20245007杨悦
from definite import connect 
def f1(x):
    return 1+x

def f2(x):
    return 1/(1+4*x**2)
print("%.2f" % connect(f1,0,2,100))
print("%.2f" % connect(f2,-1,1,100))
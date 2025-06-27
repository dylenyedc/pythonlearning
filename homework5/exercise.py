n=int(input())
a=100.0
b=100.0
for i in range(0,n):
    if(i%5<3):
        a=a*1.002
    else:
        a=a*0.999
    b=b*1.001
print("{1:.5f},{0:.5f}".format(a,b))
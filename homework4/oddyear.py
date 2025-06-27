y=int(input())
if y%4==0:
    if y%400==0:
        print("闰年")
    elif y%100 ==0:
        print("平年")
    else:
        print("闰年")
else:
    print("平年")
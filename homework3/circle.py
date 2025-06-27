import math
r = eval((input("请输入圆的半径：")))
a = math.pi * r * r
p = 2 * math.pi * r
print("周长：{:.2f}面积：{:.2f}".format(p,a))
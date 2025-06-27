def classify(listT):
    a,b,c,d= [], [], [], []
    """对应聘者进行分类"""
    for m in listT:
        interview = int(m[1])
        test = int(m[2])
        if interview>=60 and test>=60:
            if interview>=80 and test>=80:
                a.append(m)
            elif interview>=80:
                b.append(m)
            elif interview>=test:
                c.append(m)
            else:
                d.append(m)
    return a,b,c,d
def admissionSort(a,b,c,d):
    listA=[]
    for i in (a,b,c,d):
        i.sort(key=lambda x : (-(int(x[1])+int(x[2])),-int(x[1]),int(x[0])))
        listA.extend(i)
    """将分类后的应聘者按录取顺序排列"""
    return listA
    
    


def getdata( ):
    """从文件读取应聘者信息"""
    s = []
    while True:
        line = input()
        if not line:
            break 
        s.append(line.split())
    return s

#在此处定义两个函数

def myPrintL(listA):
    """输出录取人数和按录取顺序排列的应聘者名单"""
    print("上线人数",len(listA))
    for j in listA:
        print(" ".join(j))

def main():
    listA = getdata()#获取原始数据
    a, b, c, d = classify(listA)
    admissionList=admissionSort( a, b, c, d)#生成录取顺序名单
    myPrintL(admissionList)

main()
datas='university/university1.txt'
university={}
with open(datas,'r', encoding='utf-8') as files:
    for line in files:
        datapairs=line.split()
        key,value1,value2,value3,value4=datapairs
        university[key]=(value1,value2,value3,value4)
provience=input()
print(f"{provience}大学数量:{university[provience][0]},双一流高校建设数量:{university[provience][1]}一流大学建设高校数量:{university[provience][2]}一流学科建设高校数量{university[provience][3]}")
sorteduniversity=sorted(university.items(),key=lambda x:(x[1][1],x[1][2]),reverse=True)
doublegood=0
good=0
for groups in sorteduniversity:
    print(f"{groups[0]}有{groups[1][0]}所大学，{groups[1][1]}所双一流高校，{groups[1][2]}所一流大学，{groups[1][3]}所一流学科建设高校。")
    doublegood+=int(groups[1][1])
    good+=int(groups[1][2])
print(f"中国共有{doublegood}所双一流高校，{good}所一流大学。")
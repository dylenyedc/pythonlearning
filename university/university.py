datas='university/university.txt'
university={}
with open(datas,'r', encoding='utf-8') as files:
    for line in files:
        datapair=line.split()
        key,value=datapair
        university[key]=value
sorteduniversity=sorted(university.items(),key=lambda x:x[1],reverse=True)
rank=0
for groups in sorteduniversity:
    rank+=1
    print(f"大学数量第{rank}多的省是{groups[0]},为{groups[1]}所")
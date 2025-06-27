t1 = input()
t = str.split(t1)
re =(int(t[2])-int(t[0]))*60+int(t[3])-int(t[1])
minute = re%60
hour = re//60
print(hour,":",minute,sep="")
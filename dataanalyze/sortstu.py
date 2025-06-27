#列表students记录了多名学生信息，每名学生包含姓名，成绩，年龄
students = [('John','A',25), ('Mike',"C",19),
            ('Mike',"B",12), ('Mike','C',18),
            ('Bom','D',10),  ('Mike','D',19)]

stuA = students.copy()
stuA.sort()
print(stuA)

def myKey(x):
    return int(x[2])%10  # 按姓名、成绩、年龄排序

stuB = sorted(students,key = myKey)
print(stuB)

stuC = sorted(students,key = lambda x:ord(x[1]))  # 按年龄降序排序
print(stuC)

def myKey2(x):
    return (-x[2],x[1])

students.sort(key = myKey2)
print(students)